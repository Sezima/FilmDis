from django.db import models

# Create your models here.

'''create model'''


class Genre(models.Model):
    title_genre = models.CharField(max_length=300, blank=True, null=True)


class Film(models.Model):
    title = models.CharField(max_length=500, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True);
    image = models.ImageField(blank=True, null=True)
    country = models.CharField(max_length=500, blank=True, null=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='genre', blank=True, null=True)
    description = models.TextField(blank=True, null=True)


    def name_film(self):
        return self.title





