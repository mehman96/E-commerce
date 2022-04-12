from django.contrib import admin

from . models import Blog,Author,Commenter

class BlogAdmin(admin.ModelAdmin):
   list_display = ['author', 'author_comment']
   prepopulated_fields = {'slug': ('image',)}


admin.site.register(Blog, BlogAdmin)
admin.site.register(Author)
admin.site.register(Commenter)