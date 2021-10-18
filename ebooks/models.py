from django.core import validators
from django.db import models
from django.db.models.fields import DateField
from django.core.validators import MinValueValidator, MaxValueValidator


class Ebook(models.Model):
    title            = models.CharField(max_length=140)
    author           = models.CharField(max_length=60)
    description      = models.TextField()
    publication_date = DateField()

    def __str__(self):
        return self.title

class Review(models.Model):
    created_at    = models.DateTimeField(auto_now_add=True)
    updated       = models.DateTimeField(auto_now=True)
    review_author = models.CharField(max_length=8, blank=True, null=True)
    review        = models.TextField(blank=True, null=True)
    rating        = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    ebook         = models.ForeignKey(Ebook, on_delete=models.CASCADE, related_name="reviews")

    def __str__(self):
        return str(self.rating)