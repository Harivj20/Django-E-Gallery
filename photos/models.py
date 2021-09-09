from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=500,blank=True,null=True)

    def __str__(self):
        return self.name

class Photo(models.Model):
    category=models.ForeignKey(Category, on_delete=models.SET_NULL,null=True)
    image=models.FileField(upload_to='image/')
    description=models.TextField()

    def __str__(self):
        return self.description

class Theme(models.Model):
    color=models.CharField(max_length=500)
    user=models.CharField(max_length=500)

    def __str__(self):
        return self.user        
