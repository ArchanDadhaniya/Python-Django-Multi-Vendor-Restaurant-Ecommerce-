

from . import views
from django.urls import include, path


urlpatterns = [
    path('',views.myAccount, name='myAccount'),
    path('registerUser/', views.registerUser, name='registerUser'),
    path('registerVendor/', views.registerVendor, name='registerVendor'),

    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('myAccount/', views.myAccount, name='myAccount'),
    path('customerDashboard/', views.customerDashboard, name='customerDashboard'),
    path('vendorDashboard/', views.vendorDashboard, name='vendorDashboard'),

    path('activate/<uidb64>/<token>/', views.activate_account, name='activate'),

    path('forgotPassword/', views.forgot_password, name='forgotPassword'), 
    path('resetPasswordValidate/<uidb64>/<token>/', views.reset_password_validate, name='resetPasswordValidate'),
    path('resetPassword/', views.reset_password, name='resetPassword'), 


    path('vendor/', include('vendor.urls')),
]