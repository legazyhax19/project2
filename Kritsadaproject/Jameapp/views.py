from django.shortcuts import render
from django.http import HttpResponse
from Jameapp.models import Person

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def gallery(request):
    return render(request, "gallery.html")

def tree(request):
    return render(request, "tree.html")

def person(request):
    all_person = Person.objects.all()
    return render(request, 'person.html', {'persons' : all_person})
