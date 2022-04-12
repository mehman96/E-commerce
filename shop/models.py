from django.db import models
from django.urls import reverse
from account.models import User
from ckeditor.fields import RichTextField
from phonenumber_field.modelfields import PhoneNumberField

class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(is_active=True)

class Category(models.Model):
    name = models.CharField(max_length=255,db_index=True)
    slug=models.SlugField(max_length=255,unique=True)

    class Meta:
        verbose_name_plural='categories'

    def get_absolute_url(self):
        return reverse('product:category_list',args=[self.slug])

    def __str__ (self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_creator')
    brand=models.CharField(max_length=225,blank=True,null=True)
    author = models.CharField(max_length=255, default='admin')
    title=models.CharField(max_length=225,blank=True,null=True)
    header=models.CharField(max_length=225,blank=True,null=True)
    image=models.ImageField(upload_to='media/')
    slug=models.SlugField(max_length=225,unique=True)
    price = models.IntegerField(blank=True,null=True)
    in_stock=models.BooleanField(default=True)
    is_active=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    products = ProductManager()
    about_desc=RichTextField(null=True, blank=True)


    class Meta:
        verbose_name_plural='Products'
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('product:product_detail',args=[self.slug])

    def __str__(self):
        return self.title




class  Checkout(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE, related_name='Checkout_user')
    first_name= models.CharField(max_length=225,blank=True,null=True)
    last_name = models.CharField(max_length=225,null=True, blank=True)
    town= models.CharField(max_length=225,null=True, blank=True)
    country= models.CharField(max_length=225,null=True, blank=True)
    phone = models.CharField(max_length=225,null=True, blank=True)
    email =models.EmailField(null=False, blank=False, unique=True)
    company = models.CharField(max_length=225,blank=True,null=True)
    address = models.CharField(max_length=225,blank=True, null=True)