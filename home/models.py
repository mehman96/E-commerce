from django.db import models




class Home(models.Model):
    image = models.ImageField(upload_to="media/")
    header=models.CharField(max_length=100, null=True,blank=True)
    desc = models.CharField(max_length=100, null=True, blank=True)
    price = models.CharField(max_length=100, null=True)


    class Meta: 
        verbose_name_plural = "Home"
     
    
    def __str__(self):
        return self.header

class Slider(models.Model):
    image = models.ImageField(upload_to="media/")
    header=models.CharField(max_length=100,blank=True,null=True)
    desc = models.CharField(max_length=100,blank=True,null=True)
    title= models.CharField(max_length=100, blank=True)


    def __str__(self):
        return self.header