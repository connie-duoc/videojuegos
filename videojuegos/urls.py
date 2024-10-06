from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Autenticación
    path('registro/', views.registro_view, name='registro'),
    path('registrado/', views.usuario_registrado_view, name='usuario_registrado'),
    path('no-registrado/', views.usuario_no_registrado_view, name='usuario_no_registrado'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Categorías
    path('categorias/', views.lista_categorias, name='lista_categorias'),
    path('categorias/crear/', views.crear_categoria, name='crear_categoria'),
    path('categorias/editar/<int:id>/', views.editar_categoria, name='editar_categoria'),
    path('categorias/eliminar/<int:id>/', views.eliminar_categoria, name='eliminar_categoria'),

    # Juegos
    path('juegos/', views.lista_juegos, name='lista_juegos'),
    path('juegos/crear/', views.crear_juego, name='crear_juego'),
    path('juegos/editar/<int:id>/', views.editar_juego, name='editar_juego'),
    path('juegos/eliminar/<int:id>/', views.eliminar_juego, name='eliminar_juego'),

    # Página de inicio
    path('', views.home_view, name='home'),
]
