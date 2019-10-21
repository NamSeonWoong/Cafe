# Create your models here.
from django.db import models
from django.conf import settings

# Create your models here.

class P(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    created_at = models.DateField(auto_now_add=True)

class C(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    p = models.ForeignKey(P,on_delete=models.CASCADE)
    content = models.CharField(max_length=200)