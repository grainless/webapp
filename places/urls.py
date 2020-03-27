from django.urls import include, path
from django.views.generic import ListView, DetailView

from places.models import Chain, Place

app_name = "places"

urlpatterns = [
    path("chains/", ListView.as_view(model=Chain), name="chain_list"),
    path("chain/<slug:slug>", DetailView.as_view(model=Chain), name="chain_detail"),
    path("places/", ListView.as_view(model=Place), name="index"),
    path(
        "place/<int:pk>/<slug:slug>/",
        DetailView.as_view(model=Place, query_pk_and_slug=True),
        name="detail",
    ),
]
