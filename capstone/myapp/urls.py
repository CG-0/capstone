from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing_page_view, name="Landing Page"),
    path("about/", views.about_view, name="About Page"),
    path("detail/<slug:slug>", views.detail_view, name="seeds-detail"),
    path("feedback/", views.feedback, name="Feedback Page"),
    path("submission/", views.submission, name="Thank You Page")
]
