from multiprocessing import context
from xml.dom import ValidationErr
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from recipe.models import User, Category, Ingredient, Recipe, UserProfile
from django.contrib.auth import authenticate, login, logout


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'description',
                  'ingredients', 'serving_size', 'category', 'image']
        widgets = {
            'ingredients': forms.CheckboxSelectMultiple(),
        }


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'weight', 'category']
        widgets = {
            'category': forms.RadioSelect(),
        }


class CategeoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "password", "email", "first_name", "last_name"]

    def clean_username(self):
        username = self.cleaned_data["username"]
        if User.objects.filter(username=username).exists():
            raise ValidationErr("Username is taken")
        return username

    def clean_password(self):
        password = self.cleaned_data["password"]
        if len(password) < 8:
            raise ValidationErr(
                "Password must be at least 8 characters long")
        return password

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

        def __init__(self, *args, **kwargs):
            super(UserEditForm, self).__init__(*args, **kwargs)
            self.fields['first_name'].label = 'First Name'
            self.fields['last_name'].label = 'Last Name'
            self.fields['email'].label = 'Email'


class UserRegistrationForm(UserCreationForm):

    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

        def __init__(self, *args, **kwargs):
            super(UserEditForm, self).__init__(*args, **kwargs)
            self.fields['first_name'].label = 'First Name'
            self.fields['last_name'].label = 'Last Name'
            self.fields['email'].label = 'Email'


class homeForm(forms.Form):
    search = forms.CharField(max_length=100, required=False)
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(), required=False)
    ingredient = forms.ModelChoiceField(
        queryset=Ingredient.objects.all(), required=False)

    def __init__(self, *args, **kwargs):
        super(homeForm, self).__init__(*args, **kwargs)
        self.fields['search'].label = 'Search'
        self.fields['category'].label = 'Category'
        self.fields['ingredient'].label = 'Ingredient'
