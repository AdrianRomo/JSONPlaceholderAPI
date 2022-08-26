from datetime import datetime

import graphene
from fastapi import FastAPI
from starlette_graphene3 import GraphQLApp, make_playground_handler

from .config.constants import API_VERSION, ENVIRONMENT
from .resources.mutations import Query, Mutations

app = FastAPI()
graphql_app = GraphQLApp(schema=graphene.Schema(query=Query, mutation=Mutations),
                         on_get=make_playground_handler())
app.mount("/graphql", graphql_app)


@app.get('/')
def ping():
    return {
        'project': 'fastapi-graphene',
        'version': API_VERSION,
        'environment': ENVIRONMENT,
        'date': str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
    }
