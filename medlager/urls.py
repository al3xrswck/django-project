from django.urls import path
from . import views
from django.views.generic.base import RedirectView

app_name = 'medlager'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
] 