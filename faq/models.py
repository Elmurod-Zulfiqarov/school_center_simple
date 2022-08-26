from django.db import models


class Certificate(models.Model):
    photo = models.ImageField(upload_to='media/')


class Review(models.Model):
    awatar = models.ImageField(upload_to='media/')
    name = models.CharField(max_length=64)
    comment = models.CharField(max_length=512)

    def __str__(self) -> str:
        return self.name


class Contact(models.Model):
    phone = models.CharField(max_length=32)
    email = models.EmailField()
    address = models.CharField(max_length=128)
    schedule = models.TextField()

    image = models.ImageField(upload_to='media/')

    def __str__(self) -> str:
        return self.email
