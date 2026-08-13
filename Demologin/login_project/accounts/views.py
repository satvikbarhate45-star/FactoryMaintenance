from django.shortcuts import render, redirect
from .models import Registration




def register(request):
    if request.method == "POST":

        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if Registration.objects.filter(email=email).exists():
            return render(
                request,
                "accounts/authenticate.html",
                {
                    "message": "Account already exists with this email!"
                }
            )

        Registration.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )

        return redirect("login")

    return render(request, "accounts/authenticate.html")


def login_view(request):

    if request.method == "POST":

        email = request.POST.get("email")
        password = request.POST.get("password")

        user = Registration.objects.filter(
            email=email,
            password=password
        ).first()

        if user:
            return render(
                request,
                "accounts/home.html",
                {"user": user}
            )

        return render(
            request,
            "accounts/authenticate.html",
            {
                "message": "Invalid Email or Password"
            }
        )

    return render(request, "accounts/authenticate.html")


def home(request):
    return render(request, "accounts/home.html")

