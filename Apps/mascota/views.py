from django.shortcuts import render, redirect
from django.http import HttpResponse
from Apps.mascota.forms import MascotaForm
from .models import Mascota

# Create your views here.

def index(request):
    return render(request,'mascota/index.html')
    #return HttpResponse('Soy la pagina principal de mascota')

def mascota_view(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
        #return redirect('mascota:index')
        return render(request,'mascota/mascota_form.html',{'form':form})
    else:
        form = MascotaForm()
    return render(request,'mascota/mascota_form.html',{'form':form})

def prueba(request):
    return render(request,'mascota/prueba.html')

def crear_mascota(request):
    if request.method == 'POST':
        mascota_form = MascotaForm(request.POST)
        if mascota_form.is_valid():
                mascota_form.save()
                return redirect('mascotaprueba')
    else:
        mascota_form=MascotaForm()
    return render(request,'mascota/prueba.html',{'mascota_form':mascota_form})

def listar_mascota(request):
    mascotas = Mascota.objects.all()
    return render(request,'mascota/listar_mascotas.html',{'mascotas':mascotas})