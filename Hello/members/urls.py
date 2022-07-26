from django.urls import path, include
from . import views
urlpatterns = [
    path('user', views.login_user, name='login'),
]