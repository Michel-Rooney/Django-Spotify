from django.db import models


class Music(models.Model):
    name = models.CharField(max_length=256)
    artist = models.CharField(max_length=256)
    cover = models.ImageField(upload_to='cover')
    song = models.FileField(upload_to='song')
    liked = models.BooleanField(default=False)

    def __str__(self):
        return self.name