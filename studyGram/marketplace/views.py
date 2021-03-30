from django.http import HttpResponse


# Create your views here.


def start(request, category=None):
    # TODO:views with category
    if category:
        return HttpResponse("Hello, world, on marketplace  "+str(category))
    return HttpResponse("Hello, world, on marketplace")
