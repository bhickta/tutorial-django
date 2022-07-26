from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('members/', include('members.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('quiz/', include('quiz.urls')),
]