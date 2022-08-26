import graphene


class GeoSchema(graphene.ObjectType):
    """Information about
    location of the place
    in latitude and longitude"""
    lat = graphene.Float()
    lng = graphene.Float()


class GeoInput(graphene.InputObjectType):
    """Input fields to update GEO location of the place, where the user lives in"""
    lat = graphene.Float(required=True)
    lng = graphene.Float(required=True)
