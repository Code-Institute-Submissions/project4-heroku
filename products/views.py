from django.shortcuts import render
from .models import Product


# Create your views here.
def all_products(request):
    return render(request, "home.html")

def all_massage(request):
    products = Product.objects.filter(category='massage')
    return render(request, "products.html", {"products": products})


def all_packages(request):
    products = Product.objects.filter(category='packages')
    return render(request, "products.html", {"products": products})

def all_face(request):
    products = Product.objects.filter(category='face')
    return render(request, "products.html", {"products": products})
