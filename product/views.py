from django.shortcuts import render,redirect,get_object_or_404
from shop.models import Category, Product


def categories(request):
      return{
         'categories': Category.objects.all()
      }


def list(request):
   products =Product.objects.all()
   context ={
      'products':products
   }
   return render(request, 'product-list.html',context)


def product_detail(request, slug):
   product=get_object_or_404(Product, slug=slug, in_stock=True)
   products =Product.objects.all()
   context ={
      'product':product,
      'products':products

   }
   return render(request, 'product-detail.html',context)


def category_list(request, category_slug=None):
   category=get_object_or_404(Category, slug=category_slug)
   products=Product.objects.filter(category=category)
   context={
      'category': category,
      'products': products
   }
   return render(request,'product-list.html',context)