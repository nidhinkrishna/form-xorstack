from django.db import models

# Create your models here.

class FormSam(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    age = models.IntegerField(null=True,blank=True)
    email = models.EmailField(null=True,blank=True)
    About = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name