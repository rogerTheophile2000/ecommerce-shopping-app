from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


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
    if request.method=="POST":
        try :
            username = request.POST['email']
            password = request.POST['password1']
            myuser= authenticate(username = username, password = password)
        except MultiValueDictKeyError:
            password = False
        if myuser is not None:
            login(request, myuser)
            messages.success(request, "Login Success")
            return render(request, "index.html")
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('/connexion/login')
    return render(request, "connexion/login.html", {})

def handlelogout(request):
    return redirect('/connexion/login')