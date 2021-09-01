from graphql_fastapi.servicos.mongo import ModMongo
from graphql_fastapi.servicos.mongo_influenciadores import MongoInfluenciadores

# with ModMongo(db='graphql') as mongo:
#     influenciadores = mongo.get_document(collection='influenciadores', visible={"nome": 1},
#                                          filter={"seguidores": {"$gte": 1000}})
#
#     for influenciador in influenciadores:
#         print(influenciador)

# with MongoConexao(db='graphql') as mongo:
#     insert = mongo.set_document(collection='influenciadores', document={"nome": "Lucas", "seguidores": 1000})
#
#     print(insert.inserted_id)

# with MongoConexao(db='graphql') as mongo:
#     resposta = mongo.update_one_document_by_id(collection='influenciadores', id='612d4125f3897bd1ddd35b22',
#                                                update={"$set": {"seguidores": 999}})
#     print(resposta)


# with MongoInfluenciadores() as mongo:
#     resultado = mongo.busca_influenciadores(campos={"seguidores": 1})
#     for r in resultado:
#         print(type(r))


from graphql_fastapi.modulos.influenciador import (
    recupera_influenciadores,
    remove_influenciador_pelo_id,
    atualiza_influenciador_pelo_id
)

print(remove_influenciador_pelo_id(id='612e56e581bfb5f4f965d68d'))
#
# print(recupera_usuarios())


from graphql_fastapi.modulos.influenciador import remove_influenciador_pelo_id

    # with MongoInfluenciadores() as mongo:
    #     result = mongo.remove_one_document_by_id(collection='influenciadores',id='612e7b909706f5c3fad0b8c0')
    #
    #     print(result)
