from django.db import models

# Create your models here.
class carousel(models.Model):
    img=models.ImageField(upload_to='media')
    txt=models.TextField()
    char=models.CharField(max_length=30)
