import json
import requests
from datetime import datetime

from django.core.management.base import NoArgsCommand
from django.core.mail import send_mail

from snapapp.models import PhotoAlbum, Photo

BASE_URL = 'https://graph.facebook.com'
FB_TOKEN = ''


class Command(NoArgsCommand):
    help = 'Create or update photo album'

    def handle(self, *args, **kwargs):
        photo_albums = PhotoAlbum.objects.filter(email_sent=False)

        for photo_album in photo_albums:

            timedelta = datetime.now() - photo_album.create_time
            if timedelta.seconds/60 > 60:
                message = '1 hr is passed since the start of the app'
                to = 'axitkhurana@gmail.com'
                self.send_email(to, message, photo_album)
                return
            result = self.fb_get_data('/me/albums', FB_TOKEN)

            for fb_album in result['data']:
                photos_added = 0
                result = self.fb_get_data('{}/photos'.format(fb_album['id']),
                                          FB_TOKEN)

                for fb_photo in result['data']:
                    try:
                        photo = Photo.objects.get(url=fb_photo['source'])
                        continue
                    except Photo.DoesNotExist:
                        photo = Photo(album=photo_album,
                                      fb_album_id=fb_album['id'],
                                      date_added=datetime.now(),
                                      url=fb_photo['source'])
                        photo.cache()
                        photo.save()
                        photos_added += 1

                    if Photo.objects.filter(album=photo_album).count() >= 12:
                        message = 'Your album is full.'
                        to = 'axitkhurana@gmail.com'
                        self.send_email(to, message, photo_album)
                        return

                    if photos_added == 5:
                        return

    def fb_get_data(self, url_path, token):
        """Returns python object from JSON data from facebook api"""
        url = '{}/{}'.format(BASE_URL, url_path)
        payload = {'access_token': FB_TOKEN, }
        r = requests.get(url, params=payload)
        result = json.loads(r.text)
        return result

    def send_email(self, to, message, photo_album):
        """Send album full/timeout email and set email sent"""
        send_mail('SnapApp: Hi!', message, 'hello@snapapp.com',
                  [to, ], fail_silently=False)
        photo_album.email_sent = True
        photo_album.save()
