from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

posts = [
	
	{
		'author':'Mike',
		'title': 'Blog Post 1',
		'content':'First Post Content',
		'date_posted':'March 21, 2024'
	
	}, 
	{
		'author':'David',
		'title': 'Blog Post 2',
		'content':'Second Post Content',
		'date_posted':'July 21, 2023'
	
	}, 
	{
		'author':'Anna',
		'title': 'Blog Post 3',
		'content':'SThird Post Content',
		'date_posted':'June 01, 2022'
	
	}


]


def index(request):
	##return HttpResponse('<h1>Welcome to our website</h1>')
	return render(request, 'blog/home.html', {'posts':Post.objects.all(), 'title':'My Home'})


def about(request):
	##return HttpResponse('<h1>This is our story .... </h1>')
	return render(request, 'blog/about.html',)