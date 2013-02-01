import json

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.core import serializers
from django.core.urlresolvers import reverse

from snapapp.models import Photo, PhotoAlbum


def index(request, album_id=None):
    if album_id is None:
        albums = PhotoAlbum.objects.all()
        return render_to_response('index.html', {'albums': albums, },
                                  context_instance=RequestContext(request))
    album = PhotoAlbum.objects.get(id=album_id)
    return render_to_response('album.html', {'album': album, },
                              context_instance=RequestContext(request))


def api(request, album_id=None):
    if album_id is None:
        albums = PhotoAlbum.objects.all()
        data = serializers.serialize('json', albums)
        return HttpResponse(data, content_type='application/json')
    album = PhotoAlbum.objects.get(id=album_id)
    data = serializers.serialize('json', album.photos.all())
    return HttpResponse(data, content_type='application/json')
