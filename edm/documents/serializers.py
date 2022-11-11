from rest_framework import serializers

from documents.models import DocKinds, DocTypes, DocTypeCategories, DocTemplates, DocRequisiteTypes, \
    DocTemplateRequisites, RequisitePossibleValues


class DocKindsSerializer(serializers.ModelSerializer):
    """Сериализация видов документов"""
    class Meta:
        model = DocKinds
        fields = '__all__'


class DocTypesSerializer(serializers.ModelSerializer):
    """Сериализация типов документов"""
    kind = serializers.SlugRelatedField(slug_field='kind',
                                        queryset=DocKinds.objects.exclude(id=1))

    class Meta:
        model = DocTypes
        fields = '__all__'


class DocTypeField(serializers.RelatedField):
    """Поле для отобржения типа документа вместе с видом"""
    def get_queryset(self):
        return DocTypes.objects.select_related('kind').exclude(id=1)

    def to_representation(self, value):
        return f'{value.type.kind} - {value.type.type}'

    def to_internal_value(self, data):
        arr = data.split(' - ')
        qs = self.get_queryset()
        return {
            'type': qs.filter(kind__kind=arr[0]).get(type=arr[1])
        }


class DocTypeCategoriesSerializer(serializers.ModelSerializer):
    """ Сериализация категорий типов документов """
    type = DocTypeField(source='*')

    class Meta:
        model = DocTypeCategories
        fields = '__all__'


class DocTemplatesListSerializer(serializers.ModelSerializer):
    """Серилизация модели шаблонов документов для списка (не все поля)"""
    category = serializers.SlugRelatedField(slug_field='category',
                                            many=True,
                                            queryset=DocTypeCategories.objects.select_related('type').exclude(id=1))

    class Meta:
        model = DocTemplates
        fields = ('id', 'category')


class DocRequisiteTypesListSerializer(serializers.ModelSerializer):
    """Сериализация типов реквизитов"""
    class Meta:
        model = DocRequisiteTypes
        fields = '__all__'


class DocRequisitesSerializer(serializers.ModelSerializer):
    """Сериализация реквизитов документов"""
    req_type = serializers.SlugRelatedField(slug_field='req_type',
                                            queryset=DocRequisiteTypes.objects.all().order_by('req_type'))

    class Meta:
        model = DocTemplateRequisites
        fields = '__all__'


class RequisitePossibleValuesSerializer(serializers.ModelSerializer):
    """Сериализация возможных значений реквизитов"""
    requisite = serializers.SlugRelatedField(slug_field='requisite',
                                             queryset=DocTemplateRequisites.objects.all())

    class Meta:
        model = RequisitePossibleValues
        fields = '__all__'


class CategoryField(serializers.RelatedField):
    """Поле для отобржения типа документа вместе с видом"""
    def get_queryset(self):
        return DocTypeCategories.objects.select_related('type').exclude(id=1)

    def to_representation(self, value):
        return f'{value.type.kind} : {value.type.type} : {value.category}'

    def to_internal_value(self, data):
        arr = data.split(' : ')
        qs = self.get_queryset()
        return {
            'type': qs.filter(type__kind__kind=arr[0]).get(type__type=arr[1])
        }


class DocTemplatesListSerializer(serializers.ModelSerializer):
    """Сериализация шаблона документа для списка"""
    category = CategoryField(source='*')

    class Meta:
        model = DocTemplates
        fields = ('id', 'category', 'date_create', 'name', 'doc')


