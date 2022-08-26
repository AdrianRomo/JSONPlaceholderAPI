from typing import Optional, List

from graphene_pydantic import PydanticInputObjectType, PydanticObjectType
from pydantic import BaseModel

from .geo import GeoModel


class AddressModel(BaseModel):
    street: Optional[str]
    suite: Optional[str]
    city: Optional[str]
    zipcode: Optional[str]
    geo: Optional[List[GeoModel]]


class AddressGrapheneModel(PydanticObjectType):
    class Meta:
        model = AddressModel


class AddressGrapheneInputModel(PydanticInputObjectType):
    class Meta:
        model = AddressModel
        exclude_fields = ('id',)