
from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('item/<slug:slug>/', views.product_detail, name='product_detail'),
    path('list/', views.list , name='product_list'),
    path('item/<slug:category_slug>/', views.category_list, name='category_list'),
]


