from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    description = models.TextField(max_length=400)
    price = models.IntegerField()
    category = models.CharField(max_length=50)
    reviews = models.TextField(max_length=400)

    def __str__(self):
        return self.name