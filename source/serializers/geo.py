from graphene_pydantic import PydanticInputObjectType, PydanticObjectType
from pydantic import BaseModel


class GeoModel(BaseModel):
    lat: float
    lng: float


class GeoGrapheneModel(PydanticObjectType):
    class Meta:
        model = GeoModel


class GeoGrapheneInputModel(PydanticInputObjectType):
    class Meta:
        model = GeoModel
        exclude_fields = ('id',)