from django.urls import path
from django.views.generic import ListView, DetailView

from places.models import Place

app_name = "places"

urlpatterns = [
    path("", ListView.as_view(model=Place), name="index"),
    path("place/<slug:slug>/", DetailView.as_view(model=Place), name="detail"),
]
