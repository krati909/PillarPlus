from django.db import models


# Create your models here.
class testdata(models.Model):
    field_name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    options = models.CharField(max_length=50)
    mandatory = models.CharField(max_length=50)
    subject = models.TextField()


