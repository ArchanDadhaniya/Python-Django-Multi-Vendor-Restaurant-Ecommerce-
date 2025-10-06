from django.shortcuts import redirect, render

from accounts.forms import UserForm
from accounts.models import User
from django.contrib import messages 

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