from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string


menu = [
    {'title': "About this web", 'url_name': 'about'},
    {'title': "Add an article", 'url_name': 'add_page'},
    {'title': "Contact us", 'url_name': 'contact'},
    {'title': "Login", 'url_name': 'login'},
]

data_db = [
    {'id': 1, 'title': 'Angelina Jolie', 'content': "<h1>Angelina Jolie</h1> born June 4, 1975 is an American actress, "
                                                    "filmmaker, and humanitarian. The recipient of numerous accolades, "
                                                    "including an Academy Award, a Tony Award and three Golden Globe Awards,"
                                                    " she has been named Hollywood's highest-paid actress multiple times.",
     'is_published': True},
    {'id': 2, 'title': 'Brad Pitt', 'content': '<h1>Brad Pitt</h1> is an American actor.', 'is_published': False},
    {'id': 3, 'title': 'Demi Moore', 'content': '<h1>Demi Moore</h1> is an American actress.', 'is_published': True},
]

cats_db = [
    {'id': 1, 'name': 'Actress'},
    {'id': 2, 'name': 'Singer'},
    {'id': 3, 'name': 'Sportsmans'},
]


def index(request): # HttpRequest

    data = {'title': "The main page of the site",
            'menu': menu,
            'posts': data_db,
            'cat_selected': 0,
            }
    return render(request, 'women/index.html', context=data)

def about(request):
    return render(request, 'women/about.html', {'title': "About this web", 'menu': menu})

def show_post(request, post_id):
    return HttpResponse(f"Displaying the article with id = {post_id}")

def addpage(request):
    return HttpResponse("Add page")

def contact(request):
    return HttpResponse("Contact us")

def login(request):
    return HttpResponse("Login")

def show_category(request, cat_id):
    data = {
        'title': "The main page of the site",
        'menu': menu,
        'posts': data_db,
        'cat_selected': cat_id,
    }
    return render(request, 'women/index.html', context=data)

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Page not found</h1>")
