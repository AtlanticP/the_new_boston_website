from django.http import Http404
from django.shortcuts import render
from .models import Album

from .models import Album 

def index(request):
	all_albums = Album.objects.all()
	html = ''
	context = {'all_albums' : all_albums}
	return render(request, 'app/index.html', context)

def details(request, album_id):
	try:
		album = Album.objects.get(pk=album_id)
	except:
		raise Http404("Album does not exist")
