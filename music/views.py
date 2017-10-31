from django.http import HttpResponse
from django.shortcuts import render
from .models import Album

from .models import Album 

def index(request):
	all_albums = Album.objects.all()
	html = ''
	context = {'all_albums' : all_albums}
	return render(request, 'app/index.html', context)

def details(request, album_id):
	return HttpResponse("<h2>Details for album id: " + str(album_id) + '<h2>')
