
from django.urls import path
from .views import feedback

app_name="contact"

urlpatterns = [
    path('', feedback, name='feedback'),
 
]

