from django.db import models
from users.models import User
# Create your models here.
class Book(models.Model):
    STATUS = (
        ('available', 'available'),
        ('borrowed', 'borrowed'),
    )
    title = models.CharField(max_length=100)
    availability = models.CharField(max_length=9, choices=STATUS, default='available')
    borrowedByUser = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title
    