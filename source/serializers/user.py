from typing import Optional, List

from graphene_pydantic import PydanticInputObjectType, PydanticObjectType
from pydantic import BaseModel

from .address import AddressModel
from .company import CompanyModel


class UserModel(BaseModel):
    id: int
    name: Optional[str]
    username: Optional[str]
    email: Optional[str]
    address: Optional[List[AddressModel]]
    phone: Optional[str]
    website: Optional[str]
    company: Optional[List[CompanyModel]]


class UserGrapheneModel(PydanticObjectType):
    class Meta:
        model = UserModel


class UserGrapheneInputModel(PydanticInputObjectType):
    class Meta:
        model = UserModel
        exclude_fields = ('id',)