from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
def country(request):
    return HttpResponse("This is our country India function")
def person(request):
    return HttpResponse('<h1><marquee> I am Baisali Das , i will fulfil my dream . I am working for it...<marquee></h1>')
def maths(request):
    return HttpResponse('<h1><marquee>I am going to be data scientist definietly❤️<marquee></h1>')