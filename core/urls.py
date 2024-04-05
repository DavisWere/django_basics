from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import reverse

app_name = 'core'

urlpatterns = [
    path('register', views.register_user, name='user registration form'),
    path('', views.home, name = 'home page'), # homepage 127.0.0.1:8000
    path('home/', views.home, name = 'home page'),
    path('users', views.Display_users, name = 'available users'),
    path('login', views.login_view, name= 'login user'),
]