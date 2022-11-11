from django.http import JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, filters
from rest_framework.generics import get_object_or_404

from authen.permissions import IsAdministrator
from documents.models import DocKinds, DocTypes, DocTypeCategories, DocTemplateRequisites, DocRequisiteTypes, \
    RequisitePossibleValues, DocTemplates
from documents.serializers import DocKindsSerializer, DocTypesSerializer, DocTypeCategoriesSerializer, \
    DocRequisitesSerializer, DocRequisiteTypesListSerializer, RequisitePossibleValuesSerializer, \
    DocTemplatesListSerializer
from documents.service.additional import CreateTagRequisite


class DocKindsViewSet(viewsets.ReadOnlyModelViewSet):
    """ Просмотр видов документов """
    permission_classes = [permissions.IsAuthenticated, IsAdministrator]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['kind']
    serializer_class = DocKindsSerializer

    def get_queryset(self):
        qs = DocKinds.objects.exclude(id=1)
        if self.request.query_params.get('kind') is not None:
            qs = qs.filter(kind__contains=self.request.query_params.get('kind'))
        return qs


class DocKindsCDViewSet(viewsets.ModelViewSet):
    """ Добавление/удаление вида документа """
    permission_classes = [permissions.IsAuthenticated, IsAdministrator]
    serializer_class = DocKindsSerializer
    queryset = DocKinds.objects.exclude(id=1)

    def create(self, request, *args, **kwargs):
        new_kind = self.serializer_class(data=request.data)
        if new_kind.is_valid(raise_exception=True):
            new_kind.save()
            return JsonResponse({'success': 'Вид документа успешно добавлен'})
        else:
            return JsonResponse({'error': new_kind.errors})

    def destroy(self, request, *args, **kwargs):
        try:
            kind = get_object_or_404(self.queryset, pk=self.kwargs['pk'])
        except BaseException:
            return JsonResponse({'error': 'Вид документа не найден'})
        try:
            kind.delete()
            return JsonResponse({'success': 'Вид документа успешно удален'})
        except BaseException:
            return JsonResponse({'error': 'Произошла ошибка, повторите попытку позже'})


class DocTypesViewSet(viewsets.ReadOnlyModelViewSet):
    """ Просмотр типов документов """
    permission_classes = [permissions.IsAuthenticated, IsAdministrator]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['kind', 'type']
    serializer_class = DocTypesSerializer

    def get_queryset(self):
        qs = DocTypes.objects.exclude(id=1)
        if self.request.query_params.get('kind') is not None:
            qs = qs.filter(kind__kind__contains=self.request.query_params.get('kind'))
        if self.request.query_params.get('type') is not None:
            qs = qs.filter(type__contains=self.request.query_params.get('type'))
        return qs


class DocTypesCDViewSet(viewsets.ModelViewSet):
    """ Добавление/удаление типа документа """
    permission_classes = [permissions.IsAuthenticated, IsAdministrator]
    serializer_class = DocTypesSerializer
    queryset = DocTypes.objects.exclude(id=1)

    def create(self, request, *args, **kwargs):
        new_type = self.serializer_class(data=request.data)
        if new_type.is_valid(raise_exception=True):
            new_type.save()
            return JsonResponse({'success': 'Тип документа успешно добавлен'})
        else:
            return JsonResponse({'error': new_type.errors})

    def destroy(self, request, *args, **kwargs):
        try:
            tp = get_object_or_404(self.queryset, pk=self.kwargs['pk'])
        except BaseException:
            return JsonResponse({'error': 'Тип документа не найден'})
        try:
            tp.delete()
            return JsonResponse({'success': 'Тип документа успешно удален'})
        except BaseException:
            return JsonResponse({'error': 'Произошла ошибка, повторите попытку позже'})


class DocTypeCategoriesViewSet(viewsets.ReadOnlyModelViewSet):
    """ Просмотр категорий типов документов (список/объект) """
    permission_classes = [permissions.IsAuthenticated, IsAdministrator]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['type', 'category']
    serializer_class = DocTypeCategoriesSerializer

    def get_queryset(self):
        qs = DocTypeCategories.objects.select_related('type').exclude(id=1)
        if self.request.query_params.get('kind') is not None:
            qs = qs.filter(type__kind__kind__contains=self.request.query_params.get('kind'))
        if self.request.query_params.get('type') is not None:
            qs = qs.filter(type__type__contains=self.request.query_params.get('type'))
        if self.request.query_params.get('category') is not None:
            qs = qs.filter(category__contains=self.request.query_params.get('category'))
        return qs


class DocTypeCategoriesCDViewSet(viewsets.ModelViewSet):
    """ Добавление/удаление категории типа документа """
    permission_classes = [permissions.IsAuthenticated, IsAdministrator]
    serializer_class = DocTypeCategoriesSerializer
    queryset = DocTypeCategories.objects.exclude(id=1)

    def create(self, request, *args, **kwargs):
        new_category = self.serializer_class(data=request.data)
        if new_category.is_valid(raise_exception=True):
            new_category.save()
            return JsonResponse({'success': 'Категория типа документа успешно добавлена'})
        else:
            return JsonResponse({'error': new_category.errors})

    def destroy(self, request, *args, **kwargs):
        try:
            cat = get_object_or_404(self.queryset, pk=self.kwargs['pk'])
        except BaseException:
            return JsonResponse({'error': 'Категория типа документа не найден'})
        try:
            cat.delete()
            return JsonResponse({'success': 'Категория типа документа успешно удалена'})
        except BaseException:
            return JsonResponse({'error': 'Произошла ошибка, повторите попытку позже'})


class DocRequisiteTypesListViewSet(viewsets.ReadOnlyModelViewSet):
    """Получение списка типов ревизитов"""
    permission_classes = [permissions.IsAuthenticated, IsAdministrator]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['req_type',]
    serializer_class = DocRequisiteTypesListSerializer
    queryset = DocRequisiteTypes.objects.all()


class DocRequisitesViewSet(viewsets.ReadOnlyModelViewSet):
    """Получение списка/объекта реквизитов"""
    permission_classes = [permissions.IsAuthenticated, IsAdministrator]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['req_type', 'requisite', 'tag']
    serializer_class = DocRequisitesSerializer

    def get_queryset(self):
        qs = DocTemplateRequisites.objects.select_related('req_type').all()
        if self.request.query_params.get('requisite') is not None:
            qs = qs.filter(requisite__contains=self.request.query_params.get('requisite'))
        if self.request.query_params.get('type') is not None:
            qs = qs.filter(req_type__req_type__contains=self.request.query_params.get('type'))
        return qs


class DocRequisitesCDViewSet(viewsets.ModelViewSet):
    """ Добавление/удаление реквизита """
    permission_classes = [permissions.IsAuthenticated, IsAdministrator]
    serializer_class = DocRequisitesSerializer
    queryset = DocTemplateRequisites.objects.select_related('req_type').all()

    def create(self, request, *args, **kwargs):
        try:
            request.data.update({'tag': CreateTagRequisite(request.data['requisite'])})
        except BaseException:
            return JsonResponse({'error': 'Произошла ошибка при генерации тэга, попробуйте переименовать реквизит'})
        new_req = self.serializer_class(data=request.data)
        if new_req.is_valid(raise_exception=True):
            new_req.save()
            return JsonResponse({'success': 'Реквизит успешно добавлен'})
        else:
            return JsonResponse({'error': new_req.errors})

    def update(self, request, *args, **kwargs):
        try:
            req = get_object_or_404(self.queryset, pk=self.kwargs['pk'])
        except BaseException:
            return JsonResponse({'error': 'Реквизит не найден'})
        try:
            try:
                request.data.update({'tag': CreateTagRequisite(request.data['requisite'])})
            except BaseException:
                return JsonResponse({'error': 'Произошла ошибка при генерации тэга, попробуйте переименовать реквизит'})
            serialize = self.serializer_class(instance=req,
                                              data=request.data,
                                              many=False)
            if serialize.is_valid(raise_exception=True):
                serialize.save()
                return JsonResponse({'success': 'Реквизит успешно обновлен'})
            else:
                return JsonResponse({'error': serialize.errors})
        except BaseException:
            return JsonResponse({'error': 'Произошла ошибка, повторите попытку позже'})

    def destroy(self, request, *args, **kwargs):
        req = get_object_or_404(self.queryset, pk=self.kwargs['pk'])
        try:
            req.delete()
            return JsonResponse({'success': 'Реквизит успешно удален'})
        except BaseException:
            return JsonResponse({'error': 'Произошла ошибка, повторите попытку позже'})


class RequisitePossibleValuesViewSet(viewsets.ReadOnlyModelViewSet):
    """Получение списка возможных значений реквизита"""
    permission_classes = [permissions.IsAuthenticated, IsAdministrator]
    serializer_class = RequisitePossibleValuesSerializer

    def get_queryset(self):
        return RequisitePossibleValues.objects.\
            filter(requisite__requisite=self.request.query_params.get('req_name')).\
            order_by('possible_value')


class RequisitePossibleValueCDViewSet(viewsets.ModelViewSet):
    """Добавление/удаление возможного значения реквизита"""
    permission_classes = [permissions.IsAuthenticated, IsAdministrator]
    serializer_class = RequisitePossibleValuesSerializer
    queryset = RequisitePossibleValues.objects.all()

    def create(self, request, *args, **kwargs):
        serialize = self.serializer_class(data=request.data)
        if serialize.is_valid(raise_exception=True):
            serialize.save()
            return JsonResponse({'success': 'Значение успешно добавлено'})
        else:
            return JsonResponse({'error': serialize.errors})

    def destroy(self, request, *args, **kwargs):
        value = get_object_or_404(self.queryset, pk=self.kwargs['pk'])
        try:
            value.delete()
            return JsonResponse({'success': 'Значение успешно удалено'})
        except BaseException:
            return JsonResponse({'error': 'Произошла ошибка, повторите попытку позже'})


class DocTemplatesViewSet(viewsets.ReadOnlyModelViewSet):
    """Получение списка/объекта шаблонов документа"""
    permission_classes = [permissions.IsAuthenticated, IsAdministrator]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['category', 'date_create', 'name']
    serializer_class = DocTemplatesListSerializer
    queryset = DocTemplates.objects.select_related('category').all()