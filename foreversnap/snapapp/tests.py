import json
from datetime import datetime

from django.test import TestCase
from django.test.client import Client

from snapapp.models import Photo, PhotoAlbum


class SnapAppTest(TestCase):
    def setUp(self):
        self.album = PhotoAlbum.objects.create(create_time=datetime.now())
        self.photo1 = Photo.objects.create(album=self.album, fb_album_id='1',
                                           date_added=datetime.now(),
                                           url='http://axitkhurana.com/')
        self.photo2 = Photo.objects.create(album=self.album, fb_album_id='2',
                                           date_added=datetime.now(),
                                           url='http://google.com/')
        self.client = Client()

    def test_browser_album(self):
        """Test for response for albums page"""
        response = self.client.get('/snapapp/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['albums']), 1)

    def test_browser_photos(self):
        """Test for response for photos page"""
        album_id = self.album.id
        response = self.client.get('/snapapp/{}/'.format(album_id))
        self.assertEqual(response.status_code, 200)

        album = response.context['album']
        self.assertEqual(len(album.photos.all()), 2)

    def test_api_album(self):
        """Test for api response for albums"""
        response = self.client.get('/snapapp/api/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), [{
            'pk': 1,
            'model': 'snapapp.photoalbum',
            'fields': {
                'create_time': self.album.create_time.isoformat()[:-3],
                'email_sent': False
            }
        }])

    def test_api_photos(self):
        """Test for api response for photos"""
        album_id = self.album.id
        response = self.client.get('/snapapp/api/{}/'.format(album_id))
        self.assertEqual(response.status_code, 200)

        self.assertEqual(json.loads(response.content), [{
            'pk': 1,
            'model': 'snapapp.photo',
            'fields': {
                'album': 1,
                'photo': '',
                'fb_album_id': '1',
                'url': 'http://axitkhurana.com/',
                'date_added': self.photo1.date_added.isoformat()[:-3]
            }
        }, {
            'pk': 2,
            'model': 'snapapp.photo',
            'fields': {
                'album': 1,
                'photo': '',
                'fb_album_id': '2',
                'url': 'http://google.com/',
                'date_added': self.photo2.date_added.isoformat()[:-3]
            }
        }])
