from django.db import models

# Create your models here.
# webtoons/models.py
from django.db import models

class Webtoon(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    characters = models.TextField()

    def __str__(self):
        return self.title +"__"+ self.characters
