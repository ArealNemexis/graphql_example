from graphql_fastapi.modulos.rest.influenciador import recupera_todos_influenciadores


print(recupera_todos_influenciadores(qtd_registros_pagina=10, numero_pagina=0, campos=['nome']))