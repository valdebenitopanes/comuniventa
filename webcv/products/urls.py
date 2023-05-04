from django.urls import path
from . import views
from .views import create_product


urlpatterns =[
    #path('<pk>',ProductDetaiView.as_view(),name='product') #configurado para entero
    path('search',views.ProductSearchListView.as_view(),name='search'),
    path('<slug:slug>',views.ProductDetaiView.as_view(),name='product'),
    path('create/',create_product, name='create'),
     path('seller/',views.ProductListViewSeller.as_view(), name='seller'),
]                     