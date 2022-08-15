from multiprocessing import context
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.views import PasswordResetCompleteView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.views import PasswordResetCompleteView
from .models import Recipe
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from recipe import forms


def index(request):
    return render(request, 'index.html')


def register(request: HttpRequest) -> HttpResponse:
    form = forms.RegistrationForm()

    if request.method == "POST":
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            login(request, user)
            return redirect("home")

    context = {
        "form": form,

    }

    return render(request, "register.html", context)


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                return render(request, 'login.html', {'form': form, 'error': 'Invalid username or password'})
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('index')


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('index')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})


def reset_password(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PasswordResetForm()
    return render(request, 'reset_password.html', {'form': form})


def reset_password_confirm(request, uidb64=None, token=None):
    return PasswordResetConfirmView.as_view(template_name='reset_password_confirm.html')(request, uidb64=uidb64, token=token)


def reset_password_complete(request):
    return PasswordResetCompleteView.as_view(template_name='reset_password_complete.html')(request)


def profile(request):
    return render(request, 'profile.html')


def recipe(request):
    recipes = Recipe.objects.all()
    context = {'recipe': recipes}
    return render(request, 'recipe.html', context)


def recipe_detail(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    context = {'recipe': recipe}

    return render(request, 'recipe_detail.html', context)


def recipe_create(request):
    return render(request, 'recipe_create.html')


def recipe_edit(request, recipe_id):
    return render(request, 'recipe_edit.html')


def recipe_delete(request, recipe_id):
    return render(request, 'recipe_delete.html')


def ingredient(request):
    return render(request, 'ingredient.html')


def ingredient_detail(request, ingredient_id):
    return render(request, 'ingredient_detail.html')


def ingredient_create(request):
    return render(request, 'ingredient_create.html')


def ingredient_edit(request, ingredient_id):
    return render(request, 'ingredient_edit.html')


def ingredient_delete(request, ingredient_id):
    return render(request, 'ingredient_delete.html')


def category(request):
    return render(request, 'category.html')


def category_detail(request, category_id):
    return render(request, 'category_detail.html')


def category_create(request):
    return render(request, 'category_create.html')


def category_edit(request, category_id):
    return render(request, 'category_edit.html')


def category_delete(request, category_id):
    return render(request, 'category_delete.html')


def search(request):
    return render(request, 'search.html')


def search_result(request):
    return render(request, 'search_result.html')


def search_result_detail(request, recipe_id):
    return render(request, 'search_result_detail.html')


def search_result_create(request):
    return render(request, 'search_result_create.html')


def search_result_edit(request, recipe_id):
    return render(request, 'search_result_edit.html')


def search_result_delete(request, recipe_id):
    return render(request, 'search_result_delete.html')
