import graphene
from graphene_django.types import DjangoObjectType

from ingredients.models import Category, Ingredient


class CategoryOT(DjangoObjectType):
    class Meta:
        model = Category


class IngredientOT(DjangoObjectType):
    class Meta:
        model = Ingredient


class Query(object):
    all_categories = graphene.List(CategoryOT)
    all_ingredients = graphene.List(IngredientOT)

    def resolve_all_categories(self, info, **kwargs):
        return Category.objects.all()

    def resolve_all_ingredients(self, info, **kwargs):
        return Ingredient.objects.select_related('category').all()
