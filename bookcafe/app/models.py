from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=30)
    author=models.CharField(max_length=30)
    price=models.IntegerField()
    updated_at=models.DateTimeField(auto_now=True)
    content=models.TextField()
    cover_image_url=models.CharField(max_length=500)