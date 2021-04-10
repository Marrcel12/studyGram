from django.http import HttpResponse
from django.shortcuts import render
from .forms import SearchForm
from django.http import HttpResponseRedirect

# Create your views here.


def start(request):
    context = {"search":None}
    if request.method == 'POST':
        
        context["search"] = request.POST['search']
        form = SearchForm(request.POST)    
    else:
        form = SearchForm() 
    context["form"] = form  
    return render(request, 'index.html', context)   
