import graphene
from httpx import AsyncClient
from starlette_graphene3 import GraphQLError

from ..migrations.models.user import User

from ..schemas.user import UserInput, UserSchema


class CreateUser(graphene.Mutation):
    """Create a new user"""
    class Arguments:
        user = UserInput(required=True)

    Output = UserSchema

    @staticmethod
    async def mutate(root, info, user):
        """Save new user info
        :returns: Information about new user"""
        async with AsyncClient() as client:
            response = await client.post(
                "https://jsonplaceholder.typicode.com/users",
                json=user,
                headers={"Content-type": "application/json; charset=UTF-8"}
            )
            # Save new user info to database using only the passed fields
            user = User(**user)
            user.save()

        return response.json()


class UpdateUser(graphene.Mutation):
    """Update information about specific user"""
    Output = UserSchema

    class Arguments:
        id = graphene.ID(required=True)
        user = UserInput(required=True)

    @staticmethod
    async def mutate(root, info, id, user):
        """Update user information, using id as
        identifier
        :returns: Information about updated user"""
        async with AsyncClient() as client:
            response = await client.patch(
                f"https://jsonplaceholder.typicode.com/users/{id}",
                json=user,
                headers={"Content-type": "application/json; charset=UTF-8"}
            )
            # Update user info in database
            user = User.objects.get(id=id)
            user.name = response.json()["name"]
            user.username = response.json()["username"]
            user.email = response.json()["email"]
            user.address = response.json()["address"]
            user.phone = response.json()["phone"]
            user.website = response.json()["website"]
            user.company = response.json()["company"]
            user.update()
        return response.json()


class DeleteUser(graphene.Mutation):
    """Delete a specific user
    :returns: Deleted user information"""
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.ID(required=True)

    @staticmethod
    async def mutate(root, info, id):
        """Deletes information about user, using id as identifier and returns a boolean response"""
        async with AsyncClient() as client:
            response = await client.delete(f"https://jsonplaceholder.typicode.com/users/{id}")
            # Delete user info from database
            user = User.objects.get(id=id)
            user.delete()
        ok = True if response.status_code == 200 else False
        return DeleteUser(ok=ok)


class Query(graphene.ObjectType):
    """Query to fetch information about one or all users from the API"""
    user = graphene.Field(UserSchema, id=graphene.ID(required=True))
    users = graphene.List(UserSchema)

    @staticmethod
    async def resolve_users(root, info):
        """Fetches information about all users"""
        async with AsyncClient() as client:
            response = await client.get("https://jsonplaceholder.typicode.com/users")
        users = response.json()
        # Show all users from database and response from API
        return users

    @staticmethod
    async def resolve_user(root, info, id):
        """Fetches information about specific user, using id to identify the user"""
        async with AsyncClient() as client:
            response = await client.get(f"https://jsonplaceholder.typicode.com/users/{id}")
            # Save user info to database
            user = User(**response.json())
            user.save()
        user = response.json()
        if not user:
            raise GraphQLError(f"User with id {id} not found")
        return user


class Mutations(graphene.ObjectType):
    """Collects and provides defined mutations to be available in the API"""
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()


schema = graphene.Schema(query=Query, mutation=Mutations)
