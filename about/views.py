from django.shortcuts import render
from .models import AboutTeam






def about(request):
    teams=AboutTeam.objects.all()
    context ={
        'teams': teams,
    }
    return render( request, 'about.html',context)