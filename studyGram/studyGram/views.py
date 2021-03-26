from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {}
    # TODO:Starting page

    return render(request, 'landing.html', context)
