from django.shortcuts import render,get_object_or_404

from .models import Album 


def index(request):
	all_albums = Album.objects.all()
	return render(request, 'music/index.html', {'all_albums' : all_albums})

def details(request, album_id):
	album = get_object_or_404(Album, pk=album_id)
	return render(request, 'music/details.html', {'album' : album})

def favorite(request, album_id):
	album = get_object_or_404(Album, pk=album_id)
	try:
		selected_song = album.song_set.get(pk=request.POST['song'])
	except (KetyError, Song.DoesNotExist):
		return render(request, 'music/details.html', {
			'album': album,
			'error_message': "you did not select a valid song",
			})
	else:
		selected_song.is_favorite = True
		selected_song.save()
		return render(request, 'music/details.html', {'album': album})
