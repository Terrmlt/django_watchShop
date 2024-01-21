from django.db import models

from main.models import Brand


class Watch(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=255)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    cover = models.ImageField(upload_to='watch_covers')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.model
