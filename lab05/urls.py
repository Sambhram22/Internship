from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('solvedexercise/', include('solvedexercise.urls')),
    path('exercise01/', include('exercise01.urls')),
    path('exercise02/', include('exercise02.urls')),
]