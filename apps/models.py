from django.db import models
from django.conf import settings
from django.shortcuts import reverse

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length = 50)
    description = models.CharField(max_length=300)


class Items(models.model):
    title = models.CharField(max_length = 200)
    price = models.IntegerField()

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("apps:products", kwargs={'slug', self.slug})