from fastapi import FastAPI
from starlette.graphql import GraphQLApp
from graphene import Schema

from graphql_fastapi.mutations import Mutation
from graphql_fastapi.querys import Query

app = FastAPI()
app.add_route("/gql", GraphQLApp(
    schema=Schema(query=Query, mutation=Mutation))
              )
