from django.db import models


# Create your models here.
class Post(models.Model):
    NameTour = models.CharField(max_length=200)
    TypeTour = models.CharField(max_length=1500)
    Price = models.CharField(max_length=128)
    Photo = models.CharField(max_length=500)

    def __str__(self):
        return self.NameTour