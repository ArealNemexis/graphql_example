from graphql_fastapi.schemas.influenciador import Influenciador
from graphql_fastapi.servicos.mongo_influenciadores import MongoInfluenciadores
from graphql_fastapi.utils.utils import normaliza_id




def cria_influenciador(nome: str, seguidores: int, tags: list):
    with MongoInfluenciadores() as mongo:
        id_inserido = mongo.cadastra_influenciador(nome=nome, seguidores=seguidores, tags=tags)
        inf = Influenciador(_id=id_inserido, nome=nome, seguidores=seguidores, tags=tags)

        return inf


def recupera_influenciadores(qtd_registros_pagina: int, numero_pagina: int):
    with MongoInfluenciadores() as mongo:
        influenciadores = mongo.busca_influenciadores(qtd_registros_pagina=qtd_registros_pagina,
                                                      numero_pagina=numero_pagina)

        influenciadores = normaliza_id(influenciadores)

        return influenciadores


def recupera_influenciadores_pela_tag(tags: list, qtd_registros_pagina: int, numero_pagina: int):
    with MongoInfluenciadores() as mongo:
        influenciadores = mongo.buscar_por_tags(tags=tags, qtd_registros_pagina=qtd_registros_pagina,
                                                numero_pagina=numero_pagina)

        influenciadores = normaliza_id(influenciadores)

        return influenciadores


def recupera_influenciador_pelo_nome(nome: str):
    with MongoInfluenciadores() as mongo:
        return mongo.busca_influenciador_por_nome(nome=nome)


def recupera_influenciador_pelo_id(id: str):
    with MongoInfluenciadores() as mongo:
        return mongo.busca_influenciador_por_id(id=id)


def remove_influenciador_pelo_id(id: str):
    with MongoInfluenciadores() as mongo:
        return mongo.remover_by_id(id)


def atualiza_influenciador_pelo_id(id: str, campos: dict):
    with MongoInfluenciadores() as mongo:
        return mongo.update_by_id(id=id, campos=campos)
