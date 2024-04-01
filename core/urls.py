from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import reverse

app_name = 'core'

urlpatterns = [
    path('user/', views.create_user, name='user registration form'),
    path('user_profile', views.user_profile, name = 'profile')
]