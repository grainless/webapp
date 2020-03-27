from django.shortcuts import get_object_or_404
from django.views.generic import ListView

from places.models import Place
from reviews.models import Review


class ReviewsList(ListView):
    def get_queryset(self):
        self.place = get_object_or_404(
            Place, slug=self.kwargs["slug"], id=self.kwargs["id"]
        )

        return Review.objects.filter(place=self.place)
