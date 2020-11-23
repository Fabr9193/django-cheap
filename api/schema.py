from graphene import ObjectType, Schema

import users.schema
import flights.schema

import graphene
import graphql_jwt

class Query(users.schema.Query, flights.schema.Query , ObjectType):
    pass
class Mutation(users.schema.Mutation, flights.schema.Mutation,ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    pass


schema = Schema(query=Query, mutation=Mutation)
