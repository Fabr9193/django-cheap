from graphene import ObjectType, Schema

from flights.schema import schema
from users.schema import schema

import graphene
import graphql_jwt

class Query(schema.Query, ObjectType):
    pass
class Mutation(schema.Mutation, ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    pass


schema = Schema(query=Query, mutation=Mutation)
