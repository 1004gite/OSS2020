from django.db import models

# Create your models here.


class Note(models.Model):
    memo = models.CharField(max_length=255, unique=False)
    latitudes = models.FloatField(max_length=10)
    longitudes = models.FloatField(max_length=10)
    created = models.DateTimeField(auto_created=True, auto_now_add=True)

    def __str__(self):
        return self.memo
