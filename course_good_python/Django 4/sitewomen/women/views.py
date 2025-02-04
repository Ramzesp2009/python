from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string
# import requests

manu = ["About this web", "Add an artickle", "Contact us", "Login", "Register"]

class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

def index(request): # HttpRequest
    # t = render_to_string('women/index.html')
    # return HttpResponse(t)
    data = {'title': "The main page of the site",
            'manu': manu,
            'float': 28.56,
            'lst': [1, 2, 3, 4, 5],
            'set': {1, 2, 3, 4, 5},
            'dict': {
                'key1': 'value1',
                'key2': 'value2'
            },
            'obj': MyClass(10,20),
            }
    return render(request, 'women/index.html', context=data)

def about(request):
    return render(request, 'women/about.html', {'title': "About this web"})

def cats(request, cat_id):
    return HttpResponse(f"<h1>The articles by categories</h1><p>id: {cat_id}</p>")

def categories(request, cat_id):
    return HttpResponse(f"<h1>The articles by categories</h1><p>id: {cat_id}</p>")

def categories_by_slug(request, cat_slug):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>The articles by categories</h1><p>slug: {cat_slug}</p>")

def archive(request, year):
    if year > 2023:
        url = reverse('cats', args=('sport', ))
        return HttpResponsePermanentRedirect(url)

    return HttpResponse(f"<h1>Archive</h1><p>year: {year}</p>")

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Page not found</h1>")
