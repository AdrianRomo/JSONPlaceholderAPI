import graphene


class CompanySchema(graphene.ObjectType):
    """Provides information about company in which the user works in"""
    name = graphene.String()
    catchPhrase = graphene.String()
    bs = graphene.String()


class CompanyInput(graphene.InputObjectType):
    """Input fields to update information about company, where the user works in"""
    name = graphene.String(required=True)
    catchPhrase = graphene.String()
    bs = graphene.String()