from django.db import models
from django.db.models import  DateTimeField
from django.utils.timezone import now
from django.urls import reverse
from ckeditor.fields import RichTextField


class Author(models.Model):
        author = models.CharField(max_length=127, null=True, blank=True)
        slug=models.SlugField(max_length=255,unique=True)

        class Meta:
          verbose_name_plural ='Authors' 
                
                
        def get_absolute_url(self):
                return reverse('blog:blog_list',args=[self.slug])     

        def __str__ (self):
                return self.author

class Blog(models.Model):
    author=models.ForeignKey(Author, related_name='blog', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/')
    created_date = models.DateTimeField(default=now, editable=True)
    author_comment = RichTextField(null=True, blank=True)
    slug = models.SlugField(null=True) 
    
    
    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

    def get_absolute_url(self):
        return reverse('blog:blog_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.author_comment


class Commenter(models.Model):
    name=models.CharField(null=True,blank=True,max_length=255)
    email=models.EmailField(null=True, blank=True)
    subject=models.CharField(null=True, blank=True, max_length=255)
    comment=models.CharField(null=True, blank=True, max_length=255)


    def __str__(self):
        return self.name