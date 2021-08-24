from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    NameTour = models.CharField(max_length=200)
    TypeTour = models.CharField(max_length=1500)
    Price = models.CharField(max_length=128)
    Photo = models.CharField(max_length=500)
    Author = models.ForeignKey(User, null=True, default=None, blank=True,
                               on_delete=models.CASCADE)
    CreationDate = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.NameTour

    class Meta:
        ordering = ["-CreationDate"]

# class Cart(models.Model):
#     UserId = models.ForeignKey(User, null=True, default=None, blank=True,
#                                on_delete=models.CASCADE)
#     ToursId = models.ForeignKey(Post, null=True, default=None, blank=True,
#                                 on_delete=models.CASCADE)
