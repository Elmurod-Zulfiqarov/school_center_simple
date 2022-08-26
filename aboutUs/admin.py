from django.contrib import admin
from .models import Home, Menu, About, AboutCource, Cource, Customer

admin.site.register([Home, Menu, About, AboutCource, Cource, Customer])
