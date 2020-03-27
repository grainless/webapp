from django.urls import include, path
from django.views.generic import DetailView

from reviews.models import Review
from reviews.views import ReviewsList

app_name = "reviews"

urlpatterns = [
    path("reviews/<int:pk>/<slug:slug>", ReviewsList.as_view(), name="list"),
    path("review/<int:pk>/", DetailView.as_view(model=Review), name="detail"),
]
