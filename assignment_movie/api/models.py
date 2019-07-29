from django.db import models

# Create your models here.


class Movie(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=False)
    year = models.IntegerField(blank=False)
    genre = models.CharField(max_length=100, blank=False)

    class Meta:
        ordering = ('created',)

    def save(self, *args, **kwargs):
        options = self.title and {'title': self.title} or {}
        super(Movie, self).save(*args, **kwargs)