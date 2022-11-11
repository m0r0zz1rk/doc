from django.urls import path

from documents.api_views import DocKindsViewSet, DocKindsCDViewSet, DocTypesViewSet, DocTypesCDViewSet, \
    DocTypeCategoriesViewSet, DocTypeCategoriesCDViewSet, DocRequisitesViewSet, DocRequisiteTypesListViewSet, \
    DocRequisitesCDViewSet, RequisitePossibleValuesViewSet, RequisitePossibleValueCDViewSet, DocTemplatesViewSet

urlpatterns = [
    path('doc_kinds/', DocKindsViewSet.as_view({'get': 'list'})),

    path('new_kind/', DocKindsCDViewSet.as_view({'post': 'create'})),
    path('delete_kind/<int:pk>', DocKindsCDViewSet.as_view({'delete': 'destroy'})),

    path('doc_types/', DocTypesViewSet.as_view({'get': 'list'})),

    path('new_type/', DocTypesCDViewSet.as_view({'post': 'create'})),
    path('delete_type/<int:pk>', DocTypesCDViewSet.as_view({'delete': 'destroy'})),

    path('doc_categories/', DocTypeCategoriesViewSet.as_view({'get': 'list'})),

    path('new_category/', DocTypeCategoriesCDViewSet.as_view({'post': 'create'})),
    path('delete_category/<int:pk>', DocTypeCategoriesCDViewSet.as_view({'delete': 'destroy'})),

    path('requisite_types/', DocRequisiteTypesListViewSet.as_view({'get': 'list'})),

    path('requisites/', DocRequisitesViewSet.as_view({'get': 'list'})),
    path('requisite/<int:pk>', DocRequisitesViewSet.as_view({'get': 'retrieve'})),

    path('new_requisite/', DocRequisitesCDViewSet.as_view({'post': 'create'})),
    path('requisite/<int:pk>/', DocRequisitesCDViewSet.as_view({'patch': 'update',
                                                               'delete': 'destroy'})),

    path('req_values/', RequisitePossibleValuesViewSet.as_view({'get': 'list'})),
    path('new_value/', RequisitePossibleValueCDViewSet.as_view({'post': 'create'})),
    path('delete_value/<int:pk>', RequisitePossibleValueCDViewSet.as_view({'delete': 'destroy'})),

    path('templates/', DocTemplatesViewSet.as_view({'get': 'list'})),
]