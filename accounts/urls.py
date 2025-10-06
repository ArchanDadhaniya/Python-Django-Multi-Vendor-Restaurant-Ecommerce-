

from . import views
from django.urls import path


urlpatterns = [
    path('registerUser/', views.registerUser, name='registerUser'),
]