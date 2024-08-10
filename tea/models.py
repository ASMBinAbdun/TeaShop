from django.db import models

class Tea(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='tea/')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name
