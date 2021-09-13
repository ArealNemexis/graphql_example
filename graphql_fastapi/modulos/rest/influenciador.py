from graphql_fastapi.servicos.mongo_influenciadores import MongoInfluenciadores
from graphql_fastapi.utils.utils import normaliza_query_campos

def recupera_todos_influenciadores(qtd_registros_pagina: int = 10, numero_pagina: int = 0, campos: list = None):
    with MongoInfluenciadores() as mongo:
        return mongo.busca_influenciadores(qtd_registros_pagina=qtd_registros_pagina, numero_pagina=numero_pagina,
                                           campos=normaliza_query_campos(campos))
