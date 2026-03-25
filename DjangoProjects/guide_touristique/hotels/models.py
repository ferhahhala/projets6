# hotels/models.py
from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    wilaya = models.CharField(max_length=100, default='Tlemcen')  # Wilaya par défaut
    image = models.ImageField(upload_to='hotels/')
    price = models.IntegerField()
    google_maps_link = models.URLField()
    description = models.TextField(
        default="Aucune description disponible.",  # <-- valeur par défaut
        blank=True,  # permet de laisser vide dans l’admin
        null=True)  # <-- nouveau champ description

    def __str__(self):
        return self.name