from django.db import models
from ckeditor.fields import RichTextField


class Catalog(models.Model):
    title = models.CharField(max_length=64)
    price = models.CharField(max_length=32)
    age = models.CharField(max_length=16, null=True, blank=True)
    schedule = models.TextField(max_length=64)
    skills = RichTextField()

    def __str__(self) -> str:
        return self.title
