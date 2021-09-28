from django.db import models
from django.utils.html import mark_safe

# Create your models here.

class Banner(models.Model):
    banner=models.ImageField(upload_to='images/banners/')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)


    def banner_image(self):
        return mark_safe('<img src="/%s" width="100" height="100" />' % (self.banner))    