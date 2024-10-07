from django.shortcuts import render, redirect
from .models import Category, Game
from .forms import BuyerForm
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from .forms import LoginForm
from django.contrib.auth import authenticate, login

from .models import BuyerProfile

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Inicio de sesión exitoso.')
                return redirect('category_list')  
            else:
                messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
    else:
        form = LoginForm()
    
    return render(request, 'games/login.html', {'form': form})


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'games/category_list.html', {'categories': categories})

def category_detail(request, category_id):
    category = Category.objects.get(id=category_id)
    games = Game.objects.filter(category=category)
    return render(request, 'games/category_detail.html', {'category': category, 'games': games})


def register_buyer(request):
    if request.method == 'POST':
        form = BuyerForm(request.POST)
        if form.is_valid():
            user = form.save()
            BuyerProfile.objects.create(
                user=user,
                address=form.cleaned_data.get('address', '')
            )
            messages.success(request, 'Registro exitoso. ¡Gracias por registrarse!')
            return redirect('login')
        else:
            messages.error(request, 'Por favor, corrige los errores en el formulario.')
    else:
        form = BuyerForm()

    return render(request, 'games/register_buyer.html', {'form': form})


def thank_you(request):
    return render(request, 'games/thank_you.html')