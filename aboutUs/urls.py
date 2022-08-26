
from django.urls import path
from aboutUs.views import index

urlpatterns = [
    path('', index, name="index")
]
