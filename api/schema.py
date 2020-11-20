from graphene import ObjectType, Schema

from flights.schema import schema
from users.schema import schema

class Query(schema.Query, ObjectType):
    pass
class Mutation(schema.Mutation, ObjectType):
    pass


schema = Schema(query=Query, mutation=Mutation)
