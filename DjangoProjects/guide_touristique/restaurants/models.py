from django.db import models

class Restaurant(models.Model):
    TYPE_CHOICES = [
        ('restaurants', 'Restaurants'),
        ('fastfood', 'Fast Food'),
    ]
    name = models.CharField(max_length=200)
    wilaya = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='restaurants')
    image = models.ImageField(upload_to='restaurants/')
    google_maps_link = models.URLField()
    description = models.TextField(default="Aucune description disponible.")  # <-- ajouté

    def __str__(self):
        return self.name