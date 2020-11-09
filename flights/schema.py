import graphene
from graphene_django import DjangoObjectType
from graphene import ObjectType, Schema
from flights.models import Flight

class FlightType(DjangoObjectType):
    class Meta:
        model = Flight

class Query(ObjectType):
    flight = graphene.Field(FlightType, id=graphene.Int())
    all_flights = graphene.List(FlightType)

    def  resolve_flight(root, info, **kwargs):
        id = kwargs.get("id")
        if id is not None:
            return Flight.objects.get(id=id)
        return f"AirFrance | From:PAR | To:LIM"

    def  resolve_all_flights(root, info, **kwargs):
        return Flight.objects.all()

class FlightInput(graphene.InputObjectType):
    departure = graphene.String()
    arrival = graphene.String()
    price = graphene.Int()
    book_link = graphene.String()

class AddFlight(graphene.Mutation):
    class Arguments:
        input = FlightInput(required=True)

    flight = graphene.Field(FlightType)

    def mutate(root, info, input=None):
        flight = Flight(
            departure=input.departure,
            arrival = input.arrival,
            price= input.price,
            book_link=input.book_link
        )
        flight.save()
        return AddFlight(flight=flight)

class Mutation(graphene.ObjectType):
    add_flight = AddFlight.Field()

schema = Schema(query=Query, mutation=Mutation)