from django.shortcuts import render

from recipes.models import Recipe
from utils.recipes.factory import make_recipe


def home(request):
    recipes = Recipe.objects.all().order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
        # 'recipes': [make_recipe() for _ in range(10)],
    })


def category(request, category_id):
    recipes = Recipe.objects.filter(
        category__id=category_id
    ).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True,
    })
