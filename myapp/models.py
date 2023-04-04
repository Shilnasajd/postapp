from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Banner(models.Model):
    image=models.ImageField(upload_to="images",null=True,blank=True)
    post=models.CharField(max_length=200)

    def str(self):
        return self.post