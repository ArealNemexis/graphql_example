from pymongo import MongoClient
from bson import ObjectId
from graphql_fastapi.config import envs


class ModMongo:

    def __init__(self, db, host=envs.HOST_MONGO, port='27017'):
        conexao = f'mongodb://{host}:{port}/{db}'
        self.__client = MongoClient(conexao)
        self.__db = self.__client.get_database()

    def get_document(self, collection: str, filter: dict = None, visible: dict = None, qtd_registros_pagina: int = 10,
                     numero_pagina: int = 0):
        skip_query = ((numero_pagina - 1) * qtd_registros_pagina) if numero_pagina > 0 else 0

        resultado = self.__db[collection].find(filter, visible).sort("nome", 1).skip(skip_query).limit(
            qtd_registros_pagina)

        return [r for r in resultado]

    def set_document(self, collection: str, document: dict):
        return self.__db[collection].insert_one(document=document)

    def update_one_document_by_id(self, collection: str, id: str, update: dict):
        id = ObjectId(id)
        filter = {'_id': id}

        return self.__db[collection].update_one(filter=filter, update=update).modified_count

    def remove_one_document_by_id(self, collection: str, id: str):
        return self.__db[collection].remove({'_id': ObjectId(id)})

    def __enter__(self):
        """
        Abre a conexão com o gerenciador de contexto.
        """
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Encerra a conexão quando o objeto é destruído.
        """
        self.__client.close()
