from django.http import HttpResponse
from django.shortcuts import render
from .models import Album

from .models import Album 

def index(self):
	all_albums = Album.objects.all()
	html = ''
	for album in all_albums:
		url = '/music/' + str(album.id) + '/'
		html += '<a href="' + url + '">' + album.album_title + '</a><br>'
	return HttpResponse(html)

def details(request, album_id):
	return HttpResponse("<h2>Details for album id: " + str(album_id) + '<h2>')
