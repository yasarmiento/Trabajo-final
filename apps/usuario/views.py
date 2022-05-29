from django.shortcuts import render, redirect
from apps.usuario.formusuario import Usuarioform
from apps.usuario.formejemplares import Ejemplaresform
from apps.usuario.formprestar import Prestarform
from apps.usuario.models import Ejemplares, Prestar, Usuario

# Create your views here.

def uinicio(request):    
    usuario = Usuario.objects.all().order_by('id')
    return render(request,'paginas/usuario.html', {'usuario': usuario})

def ucreate(request):
    if request.method == 'POST':
        form = Usuarioform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('uinicio')
    else:
        form = Usuarioform()
        return render(request,'paginas/usuarioform.html', {'form': form})
    
    
def uupdate(request,id):
    usuario = Usuario.objects.get(id=id)
    if request.method == 'GET':
        form = Usuarioform(instance=usuario)
    else:
        form = Usuarioform(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('uinicio')
    return render(request, 'paginas/usuarioform.html', {'form': form})

def udelete(request, id):
    usuario = Usuario.objects.get(id=id)
    usuario.delete()
    return redirect('uinicio')

def einicio(request):    
    ejemplares = Ejemplares.objects.all().order_by('id')
    return render(request,'paginas/ejemplares.html', {'ejemplares': ejemplares})

def ecreate(request):
    if request.method == 'POST':
        form = Ejemplaresform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('einicio')
    else:
        form = Ejemplaresform()
        return render(request,'paginas/ejemplaresform.html', {'form': form})
    
    
def eupdate(request,id):
    ejemplares = Ejemplares.objects.get(id=id)
    if request.method == 'GET':
        form = Ejemplaresform(instance=ejemplares)
    else:
        form = Ejemplaresform(request.POST, instance=ejemplares)
        if form.is_valid():
            form.save()
            return redirect('einicio')
    return render(request, 'paginas/ejemplaresform.html', {'form': form})

def edelete(request, id):
    ejemplares = Ejemplares.objects.get(id=id)
    ejemplares.delete()
    return redirect('einicio')

def pinicio(request):    
    prestar = Prestar.objects.all().order_by('id')
    return render(request,'paginas/prestar.html', {'prestar': prestar})

def pcreate(request):
    if request.method == 'POST':
        form = Prestarform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pinicio')
    else:
        form = Prestarform()
        return render(request,'paginas/prestarform.html', {'form': form})
    
    
def pupdate(request,id):
    prestar = Prestar.objects.get(id=id)
    if request.method == 'GET':
        form = Prestarform(instance=prestar)
    else:
        form = Prestarform(request.POST, instance=prestar)
        if form.is_valid():
            form.save()
            return redirect('pinicio')
    return render(request, 'paginas/prestarform.html', {'form': form})

def pdelete(request, id):
    prestar = Prestar.objects.get(id=id)
    prestar.delete()
    return redirect('pinicio')