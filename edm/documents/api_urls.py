from django.urls import path

from documents.api_views import DocKindsViewSet, DocKindsCUDViewSet, DocTypesViewSet, DocTypesCUDViewSet, \
    DocTypeCategoriesViewSet, DocTypeCategoriesCUDViewSet, DocRequisitesViewSet, DocRequisiteTypesListViewSet, \
    DocRequisitesCDViewSet, RequisitePossibleValuesViewSet, RequisitePossibleValueCDViewSet, DocTemplatesViewSet

urlpatterns = [
    path('doc_kinds/', DocKindsViewSet.as_view({'get': 'list'})),

    path('new_kind/', DocKindsCUDViewSet.as_view({'post': 'create'})),
    path('edit_kind/<int:pk>', DocKindsCUDViewSet.as_view({'patch': 'update'})),
    path('delete_kind/<int:pk>', DocKindsCUDViewSet.as_view({'delete': 'destroy'})),

    path('doc_types/', DocTypesViewSet.as_view({'get': 'list'})),

    path('new_type/', DocTypesCUDViewSet.as_view({'post': 'create'})),
    path('edit_type/<int:pk>', DocTypesCUDViewSet.as_view({'patch': 'update'})),
    path('delete_type/<int:pk>', DocTypesCUDViewSet.as_view({'delete': 'destroy'})),

    path('doc_categories/', DocTypeCategoriesViewSet.as_view({'get': 'list'})),

    path('new_category/', DocTypeCategoriesCUDViewSet.as_view({'post': 'create'})),
    path('edit_category/<int:pk>', DocTypeCategoriesCUDViewSet.as_view({'patch': 'update'})),
    path('delete_category/<int:pk>', DocTypeCategoriesCUDViewSet.as_view({'delete': 'destroy'})),

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