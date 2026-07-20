
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Product, Category


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            return render(request, "login.html", {
                "error": "Invalid username or password."
            })

    return render(request, "login.html")

def dashboard(request):
    total_products = Product.objects.count()
    total_categories = Category.objects.count()

    context = {
        "total_products": total_products,
        "total_categories": total_categories,
    }

    return render(request, "dashboard.html", context)

def products(request):
    products = Product.objects.all()

    return render(request, "products.html", {
        "products": products
    })


def categories(request):
    return render(request, "categories.html")