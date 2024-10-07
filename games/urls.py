from django.urls import path
from . import views

urlpatterns = [
    path('', views.category_list, name='category_list'),
    path('category/<int:category_id>/', views.category_detail, name='category_detail'),
    path('register/', views.register_buyer, name='register_buyer'),
    path('thank-you/', views.thank_you, name='thank_you'),
    path('login/', views.login_view, name='login'),
]
