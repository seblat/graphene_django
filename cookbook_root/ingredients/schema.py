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
    category = graphene.Field(CategoryOT,
                              id=graphene.ID(),
                              name=graphene.String())
    all_categories = graphene.List(CategoryOT)

    ingredient = graphene.Field(IngredientOT,
                                id=graphene.ID(),
                                name=graphene.String())
    all_ingredients = graphene.List(IngredientOT)

    def resolve_all_categories(self, info, **kwargs):
        return Category.objects.all()

    def resolve_all_ingredients(self, info, **kwargs):
        return Ingredient.objects.select_related('category').all()

    def resolve_category(self, info, id=None, name=None, **kwargs):
        if id:
            return Category.objects.get(id=id)

        if name:
            return Category.objects.get(name=name)

        return None

    def resolve_ingredient(self, info, id=None, name=None, **kwargs):
        if id:
            return Ingredient.objects.get(id=id)

        if name:
            return Ingredient.objects.get(name=name)

        return None
