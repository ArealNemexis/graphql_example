from graphene import String, ObjectType, Int, List


class Influenciador(ObjectType):
    _id = String()
    nome = String()
    seguidores = Int()
    tags = List(String)
