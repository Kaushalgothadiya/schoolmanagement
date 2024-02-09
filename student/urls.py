from django.urls import path
from .views import SectionListCreateView,SectionViewUpdateDelete,Items_view,StudentListCreateView,StudentViewUpdateDelete,product_view
    

urlpatterns=[
    path('sections/',SectionListCreateView.as_view(),name='section-list-create'),
    path('sections/<int:id>/',SectionViewUpdateDelete.as_view(),name='section-detail'),
    path('students/',StudentListCreateView.as_view(),name='student-list-create'),
    path('students/<int:id>/',StudentViewUpdateDelete.as_view(),name='student-detail'),
    path('products/',product_view,name="product"),
    path('items/',Items_view,name='items')
]