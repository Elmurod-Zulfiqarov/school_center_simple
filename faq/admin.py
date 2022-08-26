from django.contrib import admin

from .models import Certificate, Contact, Review

admin.site.register([Certificate, Review, Contact])
