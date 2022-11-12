from . import  views
from django.urls import path
from django.conf.urls import handler404, handler500

urlpatterns = [
    path('', views.store, name='store'),
    path('category/<slug:category_slug>/', views.store, name='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('catalog/', views.store_category, name='store_category'),
    path('checkout/', views.checkout, name='checkout'),
    path('complete/', views.complete, name='complete'),
    path('search/', views.search, name='search'),
]