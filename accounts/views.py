from django.shortcuts import redirect, render

from accounts.forms import UserForm
from accounts.models import User
from django.contrib import messages

from vendor.forms import VendorForm 

# Create your views here.

def registerUser(request):
    if request.method == 'POST':
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
