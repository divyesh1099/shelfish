from django.db import models

# Create your models here.
class Book(models.Model):
    STATUS = (
        ('available', 'available'),
        ('borrowed', 'borrowed'),
    )
    title = models.CharField(max_length=100)
    availability = models.CharField(max_length=9, choices=STATUS, default='available')

    def __str__(self):
        return self.title
    