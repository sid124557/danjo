from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def inbox(request):
    return HttpResponse("<h2>wlocome to danj<h2>")
