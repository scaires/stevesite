from django.shortcuts import render

# Create your views here.
def index(request):
	context = {
		'name':'Steve',
		'title':'Hello world',
		'list':['a', 'list', 'of', 'words']
	}
	return render(request, "portfolio/index.html", context)
