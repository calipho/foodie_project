from multiprocessing import context
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from recipe.models import user, category, ingredient, recipe
from recipe.models import userProfileForm


class RecipeForm(forms.ModelForm):
    class Meta:
        model = recipe
        fields = ['name', 'description',
                  'ingredients', 'serving_size', 'category']
        widgets = {
            'ingredients': forms.CheckboxSelectMultiple(),
        }


class IngredientForm(forms.ModelForm):
    class Meta:
        model = ingredient
        fields = ['name', 'weight', 'category']
        widgets = {
            'category': forms.RadioSelect(),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = category
        fields = ['name']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = user
        fields = ['username', 'email', 'password']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = user
        fields = ['first_name', 'last_name', 'email']


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = user
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

    def rigester(self, request, user):
        user_profile = userProfile(user=user)
        user_profile.save()
        password = self.cleaned_data['password1']
        user.set_password(password)
        user.save()
        return user


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        fields = ['username', 'password']

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is None:
            raise forms.ValidationError('Invalid username or password')
        return self.cleaned_data

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Username'
        self.fields['password'].label = 'Password'


class UserEditForm(forms.ModelForm):
    class Meta:
        model = user
        fields = ['first_name', 'last_name', 'email']

        def __init__(self, *args, **kwargs):
            super(UserEditForm, self).__init__(*args, **kwargs)
            self.fields['first_name'].label = 'First Name'
            self.fields['last_name'].label = 'Last Name'
            self.fields['email'].label = 'Email'


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = userProfile
        fields = ['website', 'picture']

        def __init__(self, *args, **kwargs):
            super(ProfileEditForm, self).__init__(*args, **kwargs)
            self.fields['website'].label = 'Website'
            self.fields['picture'].label = 'Picture'
            self.fields['picture'].help_text = 'Upload a profile picture.'


class UserProfileEditForm(forms.ModelForm):
    class Meta:
        model = userProfile
        fields = ['website', 'picture']

        def __init__(self, *args, **kwargs):
            super(UserProfileEditForm, self).__init__(*args, **kwargs)
            self.fields['website'].label = 'Website'
            self.fields['picture'].label = 'Picture'
            self.fields['picture'].help_text = 'Upload a profile picture.'


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = user
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class UserEditForm(forms.ModelForm):
    class Meta:
        model = user
        fields = ['first_name', 'last_name', 'email']

        def __init__(self, *args, **kwargs):
            super(UserEditForm, self).__init__(*args, **kwargs)
            self.fields['first_name'].label = 'First Name'
            self.fields['last_name'].label = 'Last Name'
            self.fields['email'].label = 'Email'


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = userProfile
        fields = ['website', 'picture']

        def __init__(self, *args, **kwargs):
            super(ProfileEditForm, self).__init__(*args, **kwargs)
            self.fields['website'].label = 'Website'
            self.fields['picture'].label = 'Picture'
            self.fields['picture'].help_text = 'Upload a profile picture.'


class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = user
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
