from django.db import models

# Create your models here.


class Blog(models.Model):
    profile_img = models.FileField(upload_to='profile_img/', max_length=250, null=True, default=None)
    Post_title = models.CharField(max_length=100)
    discription = models.CharField(max_length=500)
