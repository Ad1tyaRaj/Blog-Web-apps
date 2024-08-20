from django.urls import path
from . import views



urlpatterns = [
    path('register/',views.Sign_up, name = 'register'),
    path('login/',views.Login,name = 'login'),
    path('profile/',views.Profile,name = 'profile'),
    path('logout/',views.Logout,name = 'logout'),
]
