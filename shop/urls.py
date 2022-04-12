
from django.urls import path
from .views import basket_summary, checkout,basket_add,basket_delete,basket_update

app_name = 'shop'

urlpatterns = [
    path('basket/', basket_summary, name='basket_summary'),
    path('add/', basket_add, name='basket_add'),
    path('checkout/', checkout, name='checkout'),
    path('delete/',basket_delete, name='basket_delete'),
    path('update/',basket_update, name='basket_update'),

    
    
]


