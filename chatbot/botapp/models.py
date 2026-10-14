

# Create your models here.
from django.db import models


class ImageRecord(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images/")
    category = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title