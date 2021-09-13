from fastapi import FastAPI
from starlette.graphql import GraphQLApp
from graphene import Schema

from graphql_fastapi.mutations import Mutation
from graphql_fastapi.querys import Query
from graphql_fastapi.rotas.influenciadores import rota_influenciadores

app = FastAPI()
app.add_route("/gql", GraphQLApp(
    schema=Schema(query=Query, mutation=Mutation))
              )

app.include_router(router=rota_influenciadores, prefix='/rest')
