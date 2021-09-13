from typing import Optional, List
from fastapi import APIRouter, Query
from graphql_fastapi.models.request_body import Campos
from graphql_fastapi.modulos.rest.influenciador import recupera_todos_influenciadores

rota_influenciadores = APIRouter()


@rota_influenciadores.get("/influenciadores")
async def all_influenciadores(campos: List[str] = Query(..., description="Identificador da mensagem"), qtd_registros_pagina: Optional[int] = 10,
                              numero_pagina: Optional[int] = 0):
    return recupera_todos_influenciadores(qtd_registros_pagina=qtd_registros_pagina, numero_pagina=numero_pagina,
                                          campos=campos)
