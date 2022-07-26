from django.urls import path
from . import views
from app import views as vw



app_name = 'authentication'
urlpatterns = [
    path('', views.sign_in, name='sing_in'),
    path('sign_up/', views.sign_up, name='sing_up'),
    path('log_out/', views.log_out, name='log_out'),
    path('profile/', vw.profile, name='profile'),
]