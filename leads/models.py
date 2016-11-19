from __future__ import unicode_literals

from django.db import models

class Lead(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.IntegerField()
    ads = models.BooleanField(default=True)

    def __str__(self):
        return self.name
