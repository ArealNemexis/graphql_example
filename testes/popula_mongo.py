from faker import Faker
from graphql_fastapi.servicos.mongo_influenciadores import MongoInfluenciadores
from random import randint, sample

fa = Faker()


def gera_tag_list():
    lista_tags = ['python', 'java', 'C', 'cpp', 'carros', 'motos', 'finanças', 'algoritmos',
                  'scrapper', 'frutas', 'jogos', 'criptomoedas', 'animais']

    return sample(lista_tags, 3)


def gena(sz):
    for i in range(sz):
        yield i


with MongoInfluenciadores() as mongo:
    for _ in gena(500000):
        try:
            mongo.cadastra_influenciador(nome=fa.name(), seguidores=randint(1, 500000), tags=gera_tag_list())
        except:
            continue
