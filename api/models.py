from django.db import models


# Create your models here.
class Game(models.Model):
    players_amount = models.PositiveIntegerField(default=2)
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
