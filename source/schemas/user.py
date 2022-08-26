import graphene

from .address import AddressSchema, AddressInput
from .company import CompanySchema, CompanyInput


class UserSchema(graphene.ObjectType):
    """Provides full information about user"""
    id = graphene.ID(required=True, description="User ID")
    name = graphene.String(description="User name", required=True)
    username = graphene.String(description="User username", required=True)
    email = graphene.String(description="User email", required=True)
    address = graphene.Field(AddressSchema, description="User address", required=True)
    phone = graphene.String(description="User phone", required=False, default_value="")
    website = graphene.String(description="User website", required=False, default_value="")
    company = graphene.Field(CompanySchema, description="User company", required=False, default_value=None)


class UserInput(graphene.InputObjectType):
    """Input fields to create a new user with the information about him/her"""
    name = graphene.String(required=True)
    username = graphene.String(required=True)
    email = graphene.String(required=True)
    phone = graphene.String(required=False, default_value="")
    website = graphene.String(required=False, default_value="")
    company = graphene.InputField(CompanyInput, required=False, default_value=None)
    address = graphene.InputField(AddressInput, required=True)