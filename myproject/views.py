from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

def about(request):
     return HttpResponse("<h1> Welcome to the about pages<h1>")
def info(request):
     return HttpResponse("<h3> Welcome to Info Page<h3>")
def default_page(request):
     return HttpResponse("<h3> Welcome to first default page <h3>")
def home(request):
     return HttpResponse("<h2> Hello Python <h2>")
def signup(request):
   return render (request,'signup.html')