from django.urls import path
# yazdigimiz functions imporr edirk
from .views import  HomeListView
app_name="home"


urlpatterns = [
    path('', HomeListView.as_view(), name='index'),
   
]