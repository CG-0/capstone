from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from .forms import FeedbackForm
from .models import Seed, Feedback

# Create your views here.
def landing_page_view(request):
    seed = Seed.objects.all().order_by('name')

    context = {
        'seeds': seed,
    }

    return render(request, "myapp/home.html", context)

def about_view(request):
    context = {
        "name": "About",
    }

    return render(request, "myapp/about.html", context)

def detail_view(request, slug):
    seed = get_object_or_404(Seed, slug=slug)

    context = {
        'name': seed.name,
        'botanical': seed.botanical,
        'seed_type': seed.seed_type,
        'continent': seed.continent
    }

    return render(request, "myapp/detail.html", context)

def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/submission')
        
    else:
        form = FeedbackForm()

    return render(request, "myapp/feedback.html", {
        "form": form,
    })

def submission(request):
    return render(request, "myapp/submission.html")