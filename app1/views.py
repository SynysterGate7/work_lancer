from django.shortcuts import render,HttpResponse
import smtplib
from app1.forms import UserRoleForm
def home(request):
    return render(request,"file1.html" )
def index(request):
    return render(request,"index.html")

# Create your views here.
