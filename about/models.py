from django.db import models



class AboutTeam(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to="media/")
    header=models.CharField(max_length=100, blank=True, )
    desc=models.CharField(max_length=100, blank=True, )
    fb_url=models.CharField(max_length=100, )
    twitter_url=models.CharField(max_length=100, )
    instagram_url=models.CharField(max_length=100,)
    is_active=models.BooleanField(default=False)


    def __str__(self):
        return self.header

        
