from django.shortcuts import render, redirect
#from apps.autor.forautor import Autorform
from apps.autor.models import Autor, Libro, Autorlibro
from apps.autor.formautor import Autorform
from apps.autor.formautorlibro import Autorlibroform
from apps.autor.formlibro import Libroform


# Create your views here.

def ainicio(request):    
    autor = Autor.objects.all().order_by('id')
    return render(request,'paginas/autor.html', {'autor': autor})

def acreate(request):
    if request.method == 'POST':
        form = Autorform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ainicio')
    else:
        form = Autorform()
        return render(request,'paginas/autorform.html', {'form': form})
    
    
def aupdate(request,id):
    autor = Autor.objects.get(id=id)
    if request.method == 'GET':
        form = Autorform(instance=autor)
    else:
        form = Autorform(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('ainicio')
    return render(request, 'paginas/autorform.html', {'form': form})

def adelete(request, id):
    autor = Autor.objects.get(id=id)
    autor.delete()
    return redirect('ainicio')

def linicio(request):    
    libro = Libro.objects.all().order_by('id')
    return render(request,'paginas/libro.html', {'libro': libro})

def lcreate(request):
    if request.method == 'POST':
        form = Libroform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('linicio')
    else:
        form = Libroform()
        return render(request,'paginas/libroform.html', {'form': form})
    
    
def lupdate(request,id):
    libro = Libro.objects.get(id=id)
    if request.method == 'GET':
        form = Libroform(instance=libro)
    else:
        form = Libroform(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('linicio')
    return render(request, 'paginas/libroform.html', {'form': form})

def ldelete(request, id):
    libro = Libro.objects.get(id=id)
    libro.delete()
    return redirect('linicio')

def alinicio(request):    
    autorlibro = Autorlibro.objects.all().order_by('id')
    return render(request,'paginas/autorlibro.html', {'autorlibro': autorlibro})

def alcreate(request):
    if request.method == 'POST':
        form = Autorlibroform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alinicio')
    else:
        form = Autorlibroform()
        return render(request,'paginas/autorlibroform.html', {'form': form})
    
    
def alupdate(request,id):
    autorlibro = Autorlibro.objects.get(id=id)
    if request.method == 'GET':
        form = Autorlibroform(instance=autorlibro)
    else:
        form = Autorlibroform(request.POST, instance=autorlibro)
        if form.is_valid():
            form.save()
            return redirect('alinicio')
    return render(request, 'paginas/autorlibroform.html', {'form': form})

def aldelete(request, id):
    autorlibro = Autorlibro.objects.get(id=id)
    autorlibro.delete()
    return redirect('alinicio')