from django.db import models
from django.contrib.auth.models import User

from places.models import Place


class Review(models.Model):
    RATINGS = ((1, "Bad"), (2, "Poor"), (3, "Average"), (4, "Good"), (5, "Excellent"))

    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="place")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    lede = models.CharField(
        blank=True, max_length=100, help_text="A short summary of your review"
    )
    body = models.TextField(max_length=500)
    rating = models.IntegerField(choices=RATINGS, default=1)

    def __str__(self):
        return f"{self.place.title} by {self.author}"

    class Meta:
        db_table = "places_review"
        app_label = "reviews"
