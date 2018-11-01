import graphene
from graphene_django import DjangoObjectType
# from gqlauth.validators import validate_username, validate_password, validate_user_is_authenticated
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .models import Category

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category

class Query(graphene.ObjectType):
    all_categories = graphene.List(CategoryType)

    def resolve_all_categories(self, info, **kwargs):
        return Category.objects.all()

# ------------------- MUTATIONS -------------------

class AddCategory(graphene.Mutation):
    message = graphene.String()

    class Arguments:
        name        = graphene.String(required=True)
        description = graphene.String(required=True)

    def mutate(self, info, name, description):
        try:
            newCategory = Category(name=name, description=description)
            newCategory.save()
            message = "success"
        except:
            message = "failure"

        return AddCategory(message)

class Mutation(object):
    addcategory = AddCategory.Field()