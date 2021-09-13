from graphql_fastapi.servicos.mongo import ModMongo
from bson import ObjectId
from graphql_fastapi.utils.utils import normaliza_id

VISIBLE = {"nome": 1, "seguidores": 1, "tags": 1}


class MongoInfluenciadores(ModMongo):
    __collection = 'influenciadores'
    __db = 'graphql'

    def __init__(self):
        super().__init__(db=self.__db)

    def cadastra_influenciador(self, nome: str, seguidores: int, tags: list):
        create = {"nome": nome, "seguidores": seguidores, "tags": tags}

        return self.set_document(self.__collection, create).inserted_id

    def busca_influenciadores(self, qtd_registros_pagina: int = 10, numero_pagina: int = 0, campos: dict = None):

        if campos is None:
            campos = VISIBLE

        retorno = [item for item in
                   self.get_document(collection=self.__collection, visible=campos,
                                     qtd_registros_pagina=qtd_registros_pagina,
                                     numero_pagina=numero_pagina)]
        try:
            if '_id' in campos.keys():
                retorno = normaliza_id(retorno)
        except KeyError as err:
            pass
        return retorno

    def busca_influenciador_por_id(self, id: str):
        return self.get_document(collection=self.__collection, filter={"_id": ObjectId(id)},
                                 visible=VISIBLE)

    def busca_influenciador_por_nome(self, nome: str):
        return self.get_document(collection=self.__collection, filter={"nome": nome},
                                 visible=VISIBLE)

    def remover_by_id(self, id: str):
        return self.remove_one_document_by_id(self.__collection, id=id)

    def update_by_id(self, id: str, campos: dict):
        if not any(map(campos.get, ['$inc', '$set', '$push', '$pop'])):
            campos = {'$set': campos}

        return self.update_one_document_by_id(collection=self.__collection, id=id, update=campos)

    def buscar_por_tags(self, tags: list, qtd_registros_pagina: int, numero_pagina: int):
        return self.get_document(collection=self.__collection, filter={"tags": {"$all": tags}},
                                 visible=VISIBLE, numero_pagina=numero_pagina,
                                 qtd_registros_pagina=qtd_registros_pagina)
