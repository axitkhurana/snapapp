import os
import urllib
from django.db import models
from django.core.files import File


class PhotoAlbum(models.Model):
    create_time = models.DateTimeField()
    email_sent = models.BooleanField()


class Photo(models.Model):
    album = models.ForeignKey(PhotoAlbum, related_name='photos')
    photo = models.ImageField(upload_to='albums/', blank=True)
    fb_album_id = models.CharField(max_length=100)
    date_added = models.DateTimeField()
    url = models.CharField(max_length=255, unique=True)

    def cache(self):
        """Store image locally if we have a URL"""
        if self.url and not self.photo:
            result = urllib.urlretrieve(self.url)
            self.photo.save(os.path.basename(self.url),
                            File(open(result[0])))
