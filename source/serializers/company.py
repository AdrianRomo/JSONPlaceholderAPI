from typing import Optional

from graphene_pydantic import PydanticInputObjectType, PydanticObjectType
from pydantic import BaseModel


class CompanyModel(BaseModel):
    name: Optional[str]
    catchPhrase: Optional[str]
    bs: Optional[str]


class CompanyGrapheneModel(PydanticObjectType):
    class Meta:
        model = CompanyModel


class CompanyGrapheneInputModel(PydanticInputObjectType):
    class Meta:
        model = CompanyModel
        exclude_fields = ('id',)