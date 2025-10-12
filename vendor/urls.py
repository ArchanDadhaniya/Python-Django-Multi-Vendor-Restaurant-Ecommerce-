
from . import views
from django.urls import include, path
from accounts import views as account_views


urlpatterns = [
    path('', account_views.vendorDashboard, name='vendor'),
    path('profile/', views.vendorProfile, name='vendorProfile'),
]