from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.conf import settings
from .models import User

@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        subject = 'Welcome to Foodies'
        message = render_to_string('foodies/welcome_email.html', {'user': instance})
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [instance.email]
        send_mail(subject, message, email_from, recipient_list)
        print('Email sent!')

# Compare this snippet from foodies/foodies/views.py:

def index(request):
    return render(request, 'foodies/index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'foodies/register.html', {'form': form})

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
                return render(request, 'foodies/login.html', {'form': form, 'error': 'Invalid username or password'})
    else:
        form = AuthenticationForm()
    return render(request, 'foodies/login.html', {'form': form})

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
    return render(request, 'foodies/change_password.html', {'form': form})

def reset_password(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PasswordResetForm()
    return render(request, 'foodies/reset_password.html', {'form': form})

def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    return render(request, 'foodies/recipe_detail.html', {'recipe': recipe})

def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user
            recipe.save()
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = RecipeForm()
    return render(request, 'foodies/recipe_create.html', {'form': form})

def recipe_edit(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user
            recipe.save()
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'foodies/recipe_edit.html', {'form': form})

def recipe_delete(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    recipe.delete()
    return redirect('index')

def ingredient_detail(request, pk):
    ingredient = Ingredient.objects.get(pk=pk)
    return render(request, 'foodies/ingredient_detail.html', {'ingredient': ingredient})

def ingredient_create(request):
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            ingredient = form.save(commit=False)
            ingredient.user = request.user
            ingredient.save()
            return redirect('ingredient_detail', pk=ingredient.pk)
    else:
        form = IngredientForm()
    return render(request, 'foodies/ingredient_create.html', {'form': form})

def ingredient_edit(request, pk):
    ingredient = Ingredient.objects.get(pk=pk)
    if request.method == 'POST':
        form = IngredientForm(request.POST, instance=ingredient)
        if form.is_valid():
            ingredient = form.save(commit=False)
            ingredient.user = request.user
            ingredient.save()
            return redirect('ingredient_detail', pk=ingredient.pk)
    else:
        form = IngredientForm(instance=ingredient)
    return render(request, 'foodies/ingredient_edit.html', {'form': form})

def ingredient_delete(request, pk):
    ingredient = Ingredient.objects.get(pk=pk)
    ingredient.delete()
    return redirect('index')

def recipe_ingredient_create(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'POST':
        form = RecipeIngredientForm(request.POST)
        if form.is_valid():
            recipe_ingredient = form.save(commit=False)
            recipe_ingredient.recipe = recipe
            recipe_ingredient.save()
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = RecipeIngredientForm()
    return render(request, 'foodies/recipe_ingredient_create.html', {'form': form})

def recipe_ingredient_edit(request, pk):
    recipe_ingredient = RecipeIngredient.objects.get(pk=pk)
    if request.method == 'POST':
        form = RecipeIngredientForm(request.POST, instance=recipe_ingredient)
        if form.is_valid():
            recipe_ingredient = form.save(commit=False)
            recipe_ingredient.recipe = recipe
            recipe_ingredient.save()
            return redirect('recipe_detail', pk=recipe_ingredient.recipe.pk)
    else:
        form = RecipeIngredientForm(instance=recipe_ingredient)
    return render(request, 'foodies/recipe_ingredient_edit.html', {'form': form})

def recipe_ingredient_delete(request, pk):
    recipe_ingredient = RecipeIngredient.objects.get(pk=pk)
    recipe_ingredient.delete()
    return redirect('index')

def ingredient_recipe_create(request, pk):
    ingredient = Ingredient.objects.get(pk=pk)
    if request.method == 'POST':
        form = IngredientRecipeForm(request.POST)
        if form.is_valid():
            ingredient_recipe = form.save(commit=False)
            ingredient_recipe.ingredient = ingredient
            ingredient_recipe.save()
            return redirect('ingredient_detail', pk=ingredient.pk)
    else:
        form = IngredientRecipeForm()
    return render(request, 'foodies/ingredient_recipe_create.html', {'form': form})

def ingredient_recipe_edit(request, pk):
    ingredient_recipe = IngredientRecipe.objects.get(pk=pk)
    if request.method == 'POST':
        form = IngredientRecipeForm(request.POST, instance=ingredient_recipe)
        if form.is_valid():
            ingredient_recipe = form.save(commit=False)
            ingredient_recipe.ingredient = ingredient
            ingredient_recipe.save()
            return redirect('ingredient_detail', pk=ingredient_recipe.ingredient.pk)
    else:
        form = IngredientRecipeForm(instance=ingredient_recipe)
    return render(request, 'foodies/ingredient_recipe_edit.html', {'form': form})

def ingredient_recipe_delete(request, pk):
    ingredient_recipe = IngredientRecipe.objects.get(pk=pk)
    ingredient_recipe.delete()
    return redirect('index')

