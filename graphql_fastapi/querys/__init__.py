from graphene import ObjectType, List, String, Int

from graphql_fastapi.modulos.influenciador import (
    recupera_influenciadores,
    recupera_influenciador_pelo_id,
    recupera_influenciador_pelo_nome,
    recupera_influenciadores_pela_tag
)
from graphql_fastapi.schemas.influenciador import Influenciador


class Query(ObjectType):
    get_influenciadores = List(Influenciador, qtd_registros_pagina=Int(default_value=10),
                               numero_pagina=Int(default_value=0))
    get_influenciador_pelo_id = List(Influenciador, id=String())

    get_influenciador_pelo_nome = List(Influenciador, nome=String())

    get_influenciadores_pelas_tags = List(Influenciador, tags=List(String),
                                          qtd_registros_pagina=Int(default_value=10),
                                          numero_pagina=Int(default_value=0))

    def resolve_get_influenciadores(self, info, qtd_registros_pagina: int, numero_pagina: int):  # noqa
        resultado = recupera_influenciadores(qtd_registros_pagina=qtd_registros_pagina, numero_pagina=numero_pagina)
        return resultado

    def resolve_get_influenciador_pelo_id(self, info, id: str):  # noqa
        resultado = recupera_influenciador_pelo_id(id=id)
        return resultado

    def resolve_get_influenciador_pelo_nome(self, info, nome: str):  # noqa
        resultado = recupera_influenciador_pelo_nome(nome=nome)
        return resultado

    def resolve_get_influenciadores_pelas_tags(self, info, tags: list, qtd_registros_pagina: int, numero_pagina: int): # noqa
        return recupera_influenciadores_pela_tag(tags=tags,
                                                 qtd_registros_pagina=qtd_registros_pagina,
                                                 numero_pagina=numero_pagina)
