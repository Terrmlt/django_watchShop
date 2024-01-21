from django.db import models

from .watch import Watch


class WatchImage(models.Model):
    id = models.AutoField(primary_key=True)
    property = models.ForeignKey(Watch, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField()
