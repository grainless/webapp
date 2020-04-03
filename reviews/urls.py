from django.urls import include, path
from django.views.generic import DetailView

from reviews.models import Review
from reviews.views import ReviewList

app_name = "reviews"

urlpatterns = [
    path("reviews/<int:pk>/<slug:slug>/", ReviewList.as_view(), name="list"),
    path("review/<int:pk>/", DetailView.as_view(model=Review), name="detail"),
]
