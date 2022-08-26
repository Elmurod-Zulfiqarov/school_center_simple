from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from aboutUs.models import Home, Menu, About, AboutCource, Cource, Customer
from catalog.models import Catalog
from faq.models import Certificate, Review, Contact
from aboutUs.forms import CustomerForm


def index(request):

    context = dict()

    if request.method == 'POST':
        form = CustomerForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            print(data)
            print(type(data))
            Customer.objects.create(
                name=data["name"],
                phone=data["phone"],
                comment=data["comment"]
            )
            return render(request, "success_message.html")

    try:
        home = Home.objects.get(pk=1)
    except Home.DoesNotExist:
        if Home.objects.all():
            home = Home.objects.all()[0]
        home = None

    try:
        contact = Contact.objects.get(pk=1)
    except Contact.DoesNotExist:
        if Contact.objects.all():
            contact = Contact.objects.all()[0]
        contact = None

    try:
        about_cource = AboutCource.objects.get(pk=1)
    except AboutCource.DoesNotExist:
        if AboutCource.objects.all():
            about_cource = AboutCource.objects.all()[0]
        about_cource = None

    # menu = Menu.objects.all()
    about = About.objects.all()
    cource = Cource.objects.all()
    catalog = Catalog.objects.all()
    certificate = Certificate.objects.all()
    review = Review.objects.all()

    form = CustomerForm()

    context = {
        "home": home,
        # "menu": menu,
        "about": about,
        "about_cource": about_cource,
        "cource": cource,
        "catalog": catalog,
        "certificate": certificate,
        "review": review,
        "contact": contact,
        "form": form
    }

    return render(request, 'index.html', context=context)
