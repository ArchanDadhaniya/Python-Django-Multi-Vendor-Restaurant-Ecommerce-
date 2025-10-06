from django.shortcuts import redirect, render

from accounts.forms import UserForm
from accounts.models import User
from django.contrib import messages, auth

from accounts.utils import detectUser
from vendor.forms import VendorForm 
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied

# Create your views here.


# Restricted the vendor from accessing the customer dashboard 
def check_role_vendor(user):
    if user.role == 1:
        return True
    else:
        raise PermissionDenied

# Restricted the customer from accessing the vendor dashboard
def check_role_customer(user):
    if user.role == 2:
        return True
    else:
        raise PermissionDenied




def registerUser(request):
    if request.user.is_authenticated:
        messages.warning(request, 'You are already registered!')
        return redirect('dashboard')
    elif request.method == 'POST':
        print(request.POST)
        form = UserForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            user = form.save(commit=False)
            user.set_password(password)
            user.role = User.CUSTOMER
            user.save()
            messages.success(request, 'Thank you for registering with us. You can now login to your account.')
            return redirect('registerUser')
        else:
            print('This is an error', form.errors)
    else:
        form = UserForm()
    context = {
        'form': form,
    }

    return render(request, 'accounts/registerUser.html', context)



def registerVendor(request):
    if request.method == 'POST':
        print(request.POST)
        form = UserForm(request.POST)
        v_form = VendorForm(request.POST, request.FILES)
        if form.is_valid() and v_form.is_valid():
            password = form.cleaned_data['password']
            user = form.save(commit=False)
            user.set_password(password)
            user.role = User.VENDOR
            user.save()

            vendor = v_form.save(commit=False)
            vendor.user = user
            vendor.user_profile = user.userprofile
            vendor.save()
            messages.success(request, 'Thank you for registering with us. You can now login to your account.')
            return redirect('registerVendor')
        else:
            print('This is an error', form.errors, v_form.errors)
    else:
        form = UserForm()
        v_form = VendorForm()

    context = {
        'form': form,
        'v_form': v_form,
    }

    return render(request, 'accounts/registerVendor.html', context)


def login(request):
    if request.user.is_authenticated:
        messages.warning(request, 'You are already logged in!')
        return redirect('myAccount')
    elif request.method == 'POST':
        print(request.POST)
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('myAccount')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('login')
    return render(request, 'accounts/login.html')

def logout(request):
    auth.logout(request)
    messages.info(request, 'You are logged out.')
    return redirect('login')

@login_required(login_url='login')
def myAccount(request):
    user = request.user
    redirectUrl = detectUser(user)
    return redirect(redirectUrl)



@login_required(login_url='login')
@user_passes_test(check_role_customer)
def customerDashboard(request):
    return render(request, 'accounts/customerDashboard.html')



@login_required(login_url='login')
@user_passes_test(check_role_vendor)
def vendorDashboard(request):
    return render(request, 'accounts/vendorDashboard.html')