from django.db import models


class Home(models.Model):
    icon = models.ImageField(upload_to='media/')
    phone = models.CharField(max_length=32)
    title = models.CharField(max_length=256)
    content = models.TextField()
    photo = models.ImageField(upload_to='media/')

    def __str__(self) -> str:
        return self.title


class Menu(models.Model):
    title = models.CharField(max_length=32)

    def __str__(self) -> str:
        return self.title


class About(models.Model):
    photo = models.ImageField(upload_to='media/')
    content = models.TextField()


class AboutCource(models.Model):
    photo = models.ImageField(upload_to='media/')
    content = models.CharField(max_length=512)


class Cource(models.Model):
    title = models.CharField(max_length=128)
    icon = models.ImageField(upload_to='media/')

    def __str__(self) -> str:
        return self.title


class Customer(models.Model):
    name = models.CharField(max_length=64)
    phone = models.IntegerField()
    comment = models.TextField()

    def __str__(self) -> str:
        return self.name
