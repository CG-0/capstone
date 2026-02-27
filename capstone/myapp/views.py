from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def landing_page_view(request):
    return HttpResponse(f"<h1>SeedBank</h1><p>Welcome to my site</p>")