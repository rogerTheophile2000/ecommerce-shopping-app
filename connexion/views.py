from django.shortcuts import render, redirect

# Create your views here.
def signup(request):
    return render(request, "connexion/signup.html", {})

def handlelogin(request):
    return render(request, "connexion/login.html", {})

def handlelogout(request):
    return redirect('/connexion/login')