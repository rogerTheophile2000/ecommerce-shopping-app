from django.shortcuts import render



# Create your views here.
def index(request):
    # return render(request, "ecommerceapp/index.html", {})
    return render(request, "index.html", {})


def contact(request):
    # return render(request, "ecommerceapp/index.html", {})
    return render(request, "ecommerceapp/contact.html", {})

def about(request):
    # return render(request, "ecommerceapp/index.html", {})
    return render(request, "ecommerceapp/about.html", {})