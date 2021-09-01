from graphene import ObjectType
from graphql_fastapi.mutations.influenciador import CreateInfluenciador, RemoveInfluenciador, UpdateInfluenciador


class Mutation(ObjectType):
    cria_influenciador = CreateInfluenciador.Field()
    remove_influenciador = RemoveInfluenciador.Field()
    atualiza_influenciador = UpdateInfluenciador.Field()
