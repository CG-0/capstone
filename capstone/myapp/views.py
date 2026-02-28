from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def landing_page_view(request):
    context = {
        "name": "Home",
    }

    return render(request, "myapp/home.html", context)

def about_view(request):
    context = {
        "name": "About",
    }

    return render(request, "myapp/about.html", context)