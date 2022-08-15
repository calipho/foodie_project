from django.contrib import admin
from .models import user, category, ingredient, recipe

admin.site.register(user)
admin.site.register(category)
admin.site.register(ingredient)
admin.site.register(recipe)
