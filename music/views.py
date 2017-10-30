from django.shortcuts import render
from django.http import HttpResponse

def index(self):
	return HttpResponse('<h1>Hellow, World!</h1>')

def details(request, album_id): # !!!!!!!! new
	return HttpResponse("<h2>Details for album id: " + str(album_id) + '<h2>')
