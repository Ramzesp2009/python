from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories


def index(request):
    context = {
        "title": "Home - Головна",
        "content": "Магазин меблів HOME",
    }

    return render(request, "main/index.html", context)


def about(request):
    context = {
        "title": "Home - Про нас",
        "content": "Про нас",
        "text_on_page": "Опис нашого магазину і чому вам саме у нас потрібно купувати.",
    }

    return render(request, "main/about.html", context)
