from django.shortcuts import render

from recipes.models import Recipe


def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
        # 'recipes': [make_recipe() for _ in range(10)],
    })


def category(request, category_id):
    recipes = Recipe.objects.filter(
        category__id=category_id,
        is_published=True,
    ).order_by('-id')

    category_name = getattr(
        getattr(recipes.first(), 'category', None),
        'name',
        'Not found'
    )

    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': f'{category_name} - Category | '
    })


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': Recipe.objects.get(id=id),
        'is_detail_page': True,
    })
