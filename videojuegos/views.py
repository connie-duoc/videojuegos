from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm
from .models import Juego, Categoria
from .forms import JuegoForm, CategoriaForm

def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('usuario_registrado')
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})

@login_required
def usuario_registrado_view(request):
    # Añadir un mensaje de bienvenida
    messages.success(request, f'Bienvenido, {request.user.username}! Has iniciado sesión correctamente.')
    return redirect('home')


def usuario_no_registrado_view(request):
    if request.user.is_authenticated:
        return redirect('usuario_registrado')
    return render(request, 'usuario_no_registrado.html')

@login_required(login_url='/login/')
def home_view(request):
    return render(request, 'home.html', {'user': request.user})

# CRUD para Categorías
def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_categorias')
    else:
        form = CategoriaForm()
    return render(request, 'crear_categoria.html', {'form': form})

def lista_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'lista_categorias.html', {'categorias': categorias})

def editar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('lista_categorias')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'editar_categoria.html', {'form': form})

def eliminar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    if request.method == 'POST':
        categoria.delete()
        return redirect('lista_categorias')
    return render(request, 'eliminar_categoria.html', {'categoria': categoria})

# CRUD para Juegos
def crear_juego(request):
    if request.method == 'POST':
        form = JuegoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_juegos')
    else:
        form = JuegoForm()
    return render(request, 'crear_juego.html', {'form': form})

def lista_juegos(request):
    juegos = Juego.objects.all()
    return render(request, 'lista_juegos.html', {'juegos': juegos})

def editar_juego(request, id):
    juego = get_object_or_404(Juego, id=id)
    if request.method == 'POST':
        form = JuegoForm(request.POST, instance=juego)
        if form.is_valid():
            form.save()
            return redirect('lista_juegos')
    else:
        form = JuegoForm(instance=juego)
    return render(request, 'editar_juego.html', {'form': form})

def eliminar_juego(request, id):
    juego = get_object_or_404(Juego, id=id)
    if request.method == 'POST':
        juego.delete()
        return redirect('lista_juegos')
    return render(request, 'eliminar_juego.html', {'juego': juego})