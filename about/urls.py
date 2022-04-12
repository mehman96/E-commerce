from django.urls import path
# from .models import AboutTeam
from .views import about

app_name="about"


urlpatterns = [
    path('', about, name='about'),
]