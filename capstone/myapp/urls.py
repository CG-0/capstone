from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing_page_view, name="Landing Page"),
    path("about/", views.about_view, name="About Page"),
]
