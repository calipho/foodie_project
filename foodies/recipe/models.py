from audioop import reverse
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class user(AbstractUser):
    pass


class category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ingredient(models.Model):
    name = models.CharField(max_length=50)
    weight = models.FloatField(default=0)
    category = models.ForeignKey(category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ingredient_detail', args=[str(self.id)])


class recipe(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    ingredients = models.ManyToManyField(ingredient)
    serving_size = models.IntegerField(default=0)
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
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


class userProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
