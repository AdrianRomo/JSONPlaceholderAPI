import graphene

from .geo import GeoSchema, GeoInput


class AddressSchema(graphene.ObjectType):
    """Provides information about location, where the user lives at"""
    street = graphene.String()
    suite = graphene.String()
    city = graphene.String()
    zipcode = graphene.String()
    geo = graphene.Field(GeoSchema, required=True)


class AddressInput(graphene.InputObjectType):
    """Input fields to updated general information about location, where the user lives in"""
    city = graphene.String(required=True)
    street = graphene.String(required=True)
    suite = graphene.String()
    zipcode = graphene.String()
    geo = graphene.InputField(GeoInput)
