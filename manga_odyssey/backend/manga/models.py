from django.db import models

class Manga(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    release_year = models.IntegerField()
    description = models.TextField()

    def str(self):
        return self.title
# Create your models here.
