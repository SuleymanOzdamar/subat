from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from .models import *

# Create your views here.
def index(request):
    kategori = ogr.objects.all()
    return render(request, "index.html", {"kategori":kategori})

def urun_goster(request,id):
    ogr = ogr2.objects.filter(kategori = id)
    return render(request, "urun_goster.html", {"ogr":ogr})

def urun_tek_goster(request,id):
    obje = ogr2.objects.filter(id = id)
    ogr = ogr2.objects.all()[:3]
    return render(request, "tek_urun.html", {"ogr":ogr, "obj":obje})


