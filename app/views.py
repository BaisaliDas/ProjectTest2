from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
def country(request):
    return HttpResponse("This is our country India function")
def changu(request):
    return HttpResponse('<h1><marquee>mangu, changu, ill beat u<marquee></h1>')