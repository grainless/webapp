from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from django.views.generic.detail import SingleObjectMixin

from places.models import Place
from reviews.models import Review


class ReviewList(ListView):
    context_object_name = "reviews"

    def get_queryset(self):
        self.place = get_object_or_404(
            Place, pk=self.kwargs["pk"], slug=self.kwargs["slug"]
        )

        return Review.objects.filter(place=self.place)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["place"] = self.place

        return context
