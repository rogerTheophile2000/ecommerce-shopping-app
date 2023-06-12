from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages



# Create your views here.
def signup(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password1']
        confirm_password = request.POST['password2']
        if password != confirm_password:
            # HttpResponse("pass incorect")
            messages.warning(request, "Password is not Matching")
            return render(request, "connexion/signup.html", {})
        try:
            if User.objects.get(username = email):
                # HttpResponse("email exist")
                messages.warning(request, "Email is taken")
                return render(request, "connexion/signup.html", {})
        except Exception as identifier:
            pass

        user = User.objects.create_user(email, email, password)
        # user.is_active = False
        user.save()
    return render(request, "connexion/signup.html", {})


def handlelogin(request):
    return render(request, "connexion/login.html", {})

def handlelogout(request):
    return redirect('/connexion/login')