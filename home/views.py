
from django.shortcuts import render
from . models import Home,Slider
from django.views.generic import ListView





class HomeListView(ListView):
    model = Home
    template_name = 'index.html'
    paginate_by = 4
    context_object_name='products'
    queryset = Home.objects.all()
  
    # multi models one list wiew
    def get_context_data(self,**kwargs):
        context=super(HomeListView,self).get_context_data(**kwargs)
        context['sliders']=Slider.objects.all()
        return context


