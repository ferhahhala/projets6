from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='hotels/')
    price = models.IntegerField()
    google_maps_link = models.URLField()

    def __str__(self):
        return self.name