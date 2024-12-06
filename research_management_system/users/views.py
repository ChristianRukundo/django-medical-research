from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserForm
from django.contrib import messages
from django import forms
from .models import CustomUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(f"Username: {username}, Password: {password}")


        user = authenticate(request, username=username, password=password)

        if user is not None:

            login(request, user)
            print("Login successful")
            return redirect('user_view')

        else:

            print("Login failed: Invalid credentials")
            messages.error(request, 'Invalid username or password.')

    return redirect('http://127.0.0.1:8000/accounts/login/')


def logout_view(request):
    user = request.user
    user.is_active = False
    user.save()
    logout(request)
    return redirect('create_user')


@login_required
def user_view(request):
    users = CustomUser.objects.all()
    return render(request, 'index.html', {'users': users})


def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            messages.success(request, 'User created successfully!')
            return redirect('user_view')
    else:
        form = UserForm()

    return render(request, 'user_form.html', {'form': form})


def user_update(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_view')
    else:
        form = UserForm(instance=user)
    return render(request, 'user_form.html', {'form': form})


def user_delete(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    if request.method == "POST":
        user.delete()
        return redirect('user_view')
    return render(request, 'user_confirm_delete.html', {'user': user})
