"""foodies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
"""foodies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from recipe import views as foodies_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', foodies_views.register, name='register'),
    path('login/', foodies_views.login_view, name='login'),
    path('logout/', foodies_views.logout_view, name='logout'),
    path('change_password/', foodies_views.change_password, name='change_password'),
    path('reset_password/', foodies_views.reset_password, name='reset_password'),
    path('recipe/<int:recipe_id>/',
         foodies_views.recipe_detail, name='recipe_detail'),
    path('profile/', foodies_views.profile, name='profile'),
    path('category/<int:pk>/', foodies_views.category_detail, name='category_detail'),
    path('search/', foodies_views.search, name='search'),
    path('search_result/', foodies_views.search_result, name='search_result'),
    path('search_result_detail/<int:pk>/',
         foodies_views.search_result_detail, name='search_result_detail'),
    path('recipe/create/', foodies_views.recipe_create, name='recipe_create'),
    path('recipe/<int:pk>/edit/', foodies_views.recipe_edit, name='recipe_edit'),
    path('recipe/<int:pk>/delete/',
         foodies_views.recipe_delete, name='recipe_delete'),
    path('ingredient/', foodies_views.ingredient, name='ingredient'),
    path('ingredient/<int:pk>/', foodies_views.ingredient_detail,
         name='ingredient_detail'),
    path('ingredient/create/', foodies_views.ingredient_create,
         name='ingredient_create'),
    path('ingredient/<int:pk>/edit/',
         foodies_views.ingredient_edit, name='ingredient_edit'),
    path('ingredient/<int:pk>/delete/',
         foodies_views.ingredient_delete, name='ingredient_delete'),
    path('category/', foodies_views.category, name='category'),
    path('category/<int:pk>/edit/',
         foodies_views.category_edit, name='category_edit'),
    path('category/<int:pk>/delete/',
         foodies_views.category_delete, name='category_delete'),
    path('category/create/', foodies_views.category_create, name='category_create'),
    path('recipe/', foodies_views.recipe, name='recipe'),



]
