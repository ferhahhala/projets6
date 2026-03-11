from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=100)
    wilaya = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='places/')
    google_maps_link = models.URLField()

    def __str__(self):
        return self.name