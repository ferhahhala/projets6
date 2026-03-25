from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=100)
    wilaya = models.CharField(max_length=100)
    image = models.ImageField(upload_to='places/')
    google_maps_link = models.URLField()
    description = models.TextField(
        default="Aucune description disponible.",  # <-- valeur par défaut
        blank=True,  # permet de laisser vide dans l’admin
        null=True)

    def __str__(self):
        return self.name