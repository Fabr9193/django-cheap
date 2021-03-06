import graphene
from graphene_django import DjangoObjectType
from graphene import ObjectType, Schema
from flights.models import Flight
from django.db.models import Q
from django.core.exceptions import ValidationError


class FlightType(DjangoObjectType):
    class Meta:
        model = Flight

class Query(ObjectType):
    flight = graphene.Field(FlightType, id=graphene.Int())
    all_flights = graphene.List(FlightType,search=graphene.String())

    def  resolve_flight(root, info, **kwargs):
        id = kwargs.get("id")
        if id is not None:
            return Flight.objects.get(id=id)
        return f"AirFrance | From:PAR | To:LIM"

    def  resolve_all_flights(root, info, search=None, **kwargs):
        if search:
            filter = (
                Q(departure__icontains=search) | Q(price__icontains=search)
            )
            return Flight.objects.filter(filter)
        return Flight.objects.all()

class FlightInput(graphene.InputObjectType):
    departure = graphene.String()
    arrival = graphene.String()
    price = graphene.Int()
    airline = graphene.String()
    duration = graphene.Int()
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
            airline= input.airline,
            duration= input.duration,
            book_link=input.book_link
        )
        flight.save()
        return AddFlight(flight=flight)

class UpdateFlight(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        flight_data = FlightInput(required=True)
    flight = graphene.Field(FlightType)

    def mutate(root, info, id,flight_data=None):
        flight = Flight.objects.get(pk=id)
        for k, v in flight_data.items():
            if v is not None:
                setattr(flight, k, v)
        try:
            flight.full_clean()
            flight.save()
            return UpdateFlight(Flight=flight)
        except ValidationError as e:
            return UpdateFlight(flight=flight, errors=e)

class DeleteFlight(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
    flight = graphene.Field(FlightType)

    def mutate(root, info, id):
        flight = Flight.objects.get(pk=id)
        try:
            if flight is not None:
                flight.delete()
                return 'ok'
        except ValidationError as e:
            return DeleteFlight(Flight=flight, errors=e)
class Mutation(graphene.ObjectType):
    add_flight = AddFlight.Field()
    update_flight = UpdateFlight.Field()
    delete_flight = DeleteFlight.Field()

schema = Schema(query=Query, mutation=Mutation)