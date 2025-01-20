from django.db import models

class Room(models.Model):
    number = models.CharField(max_length=10)
    type = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, default='free')

    def __str__(self):
        return f"Room {self.number} - {self.type}"
