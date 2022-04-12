from django.urls import path

from . import views
from blog.views import BlogListView

app_name="blog"


urlpatterns = [
    path('detail/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('', BlogListView.as_view(), name='blog_list'),
]

