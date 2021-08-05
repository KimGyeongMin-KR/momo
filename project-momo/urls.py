from django.urls import path
from . import views
# from .templates import css, js, images

urlpatterns = [
    path('register/', views.register),
    path('login/', views.login),
    path('logout/', views.logout,)
]
