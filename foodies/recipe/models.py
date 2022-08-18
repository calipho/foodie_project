from audioop import reverse
from email.mime import image
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    weight = models.FloatField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ingredient_detail', args=[str(self.id)])


class Recipe(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    instructions = models.TextField(max_length=500, default='')
    image = models.ImageField(upload_to='images/', blank=True)
    ingredients = models.ManyToManyField(Ingredient)
    serving_size = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('recipe_detail', args=[str(self.id)])

    def get_ingredients(self):
        return self.ingredients.all()

    def get_ingredient_list(self):
        return ', '.join([ingredient.name for ingredient in self.ingredients.all()])

    def get_ingredient_weight_list(self):
        return ', '.join([str(ingredient.weight) for ingredient in self.ingredients.all()])

    def get_ingredient_category_list(self):
        return ', '.join([ingredient.category.name for ingredient in self.ingredients.all()])

    def get_ingredient_category_list_id(self):
        return ', '.join([str(ingredient.category.id) for ingredient in self.ingredients.all()])

    def get_ingredient_category_list_id_weight(self):
        return ', '.join([str(ingredient.category.id) + ' ' + str(ingredient.weight) for ingredient in self.ingredients.all()])

    def get_ingredient_category_list_id_weight_name(self):
        return ', '.join([str(ingredient.category.id) + ' ' + str(ingredient.weight) + ' ' + ingredient.name for ingredient in self.ingredients.all()])

    def get_ingredient_category_list_id_weight_name_category(self):
        return ', '.join([str(ingredient.category.id) + ' ' + str(ingredient.weight) + ' ' + ingredient.name + ' ' + ingredient.category.name for ingredient in self.ingredients.all()])


class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
