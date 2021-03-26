from django.http import HttpResponse


def index(request):
    # TODO:Starting page
    return HttpResponse("Hello, world, on landing Main Page")
