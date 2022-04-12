from django.shortcuts import render,get_object_or_404
from . models import Blog,Commenter
from django.views.generic import ListView

def blog_detail(request, slug):
    blog=get_object_or_404(Blog, slug=slug)
    blogs=Blog.objects.all()
    context ={
        'blogs':blogs,
        'blog': blog,

    }
    if request.method=="POST":       
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        comment = request.POST['comment']
        user = Commenter(name=name, email=email, comment=comment,subject=subject)
        user.save()
        alert = True
        return render(request, 'blog-detail.html',{'alert':alert})
    return render(request, 'blog-detail.html',context)





class BlogListView(ListView):
   model = Blog
   template_name = 'blog-list.html'
   paginate_by = 2
   context_object_name='blogs'


