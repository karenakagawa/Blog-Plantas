from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Aqui vão suas urls
path('login/', auth_views.LoginView.as_view(
    template_name='usuarios/login.html',
    # extra_context={'titulo': 'Autenticação'} 
    ), name='login'),
# path('usuarios', include('usuarios.urls')),
path('logout/', auth_views.LogoutView.as_view(), name='logout')
]
