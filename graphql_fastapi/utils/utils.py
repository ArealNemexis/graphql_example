def normaliza_id(lista: list):
    for item in lista:
        item['_id'] = str(item['_id'])

    return lista


def normaliza_query_campos(campos: list):
    if campos is None:
        campos = ["nome"]
    campos_mostrar = dict()
    if 'id' not in campos:
        campos_mostrar['_id'] = 0
    else:
        campos_mostrar['_id'] = 1
        campos.remove('id')

    campos_mostrar.update({campo: 1 for campo in campos})

    return campos_mostrar
