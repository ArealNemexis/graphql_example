from graphene import Mutation, Field, String, Int, Boolean, List

from graphql_fastapi.modulos.influenciador import (remove_influenciador_pelo_id,
                                                   atualiza_influenciador_pelo_id,
                                                   cria_influenciador)
from graphql_fastapi.schemas.influenciador import Influenciador


class CreateInfluenciador(Mutation):
    class Arguments:
        nome = String()
        seguidores = Int()
        tags = List(String)

    influenciador = Field(Influenciador)

    def mutate(self, info, nome: str, seguidores: int = None, tags: list = None):  # noqa
        if seguidores is None:
            seguidores = 0
        if tags is None:
            tags = []

        return CreateInfluenciador(influenciador=cria_influenciador(nome=nome, seguidores=seguidores, tags=tags))


class RemoveInfluenciador(Mutation):
    class Arguments:
        id = String(required=True)
        sucess = Int()

    sucess = Field(Boolean)

    def mutate(self, info, id):  # noqa
        retorno = dict()
        retorno['sucess'] = True if remove_influenciador_pelo_id(id=id)['n'] > 0 else False

        return retorno


class UpdateInfluenciador(Mutation):
    class Arguments:
        id = String(required=True)
        nome = String()
        seguidores = Int()

    sucess = Field(Boolean)

    def mutate(self, info, id, nome: str = None, seguidores: int = None):  # noqa
        campos = dict()

        if nome:
            campos['nome'] = nome
        if seguidores:
            campos['seguidores'] = seguidores

        retorno = dict()
        retorno['sucess'] = True if atualiza_influenciador_pelo_id(id=id, campos=campos) > 0 else False

        return retorno
