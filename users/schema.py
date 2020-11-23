
from django.contrib.auth import get_user_model
import graphene
from graphene import ObjectType, Schema
from graphene_django import DjangoObjectType


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()

class Query(ObjectType):
    users = graphene.List(UserType)
    me = graphene.Field(UserType)
    def  resolve_users(root, info, **kwargs):
        return get_user_model().objects.all()

    def resolve_me(root,info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not Logged in')
        return user

class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)
    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    def mutate(root, info, username, password, email):
        user = get_user_model()(
            username = username,
            password=password,
            email=email
        )
        user.set_password(password)
        user.save()
        return CreateUser(user=user)

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()

schema = Schema(query=Query, mutation=Mutation)