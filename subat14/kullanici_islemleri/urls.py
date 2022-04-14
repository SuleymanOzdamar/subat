from django.contrib import admin
from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    path('giris/', views.giris,name="Giris"),
    path('kayit/', views.kayit,name="Kayit"),
    path('cikis/', views.cikis,name="Cikis"),
]