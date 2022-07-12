from pydoc import render_doc
from pyexpat.errors import messages
from django.shortcuts import redirect, render
from .models import *
from .forms import UserForBook
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def BookStore(request):
    book = Books.objects.all()
    return render(request,'index.html',{'book':book})


def Registration_page(request):
    form = UserForBook(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request,("User has been registerd"))
            return redirect("login")
    else:
        form= UserForBook()
    return render(request, 'register.html',{'form':form})

@login_required
def main_page(request):
    book = Books.objects.all()
    return render(request, 'main.html',{'book':book})

def logout(request):
    return render(request, 'logout.html')
