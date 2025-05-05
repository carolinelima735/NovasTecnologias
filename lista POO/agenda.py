# agenda.py

from contato import Contato
from evento import Evento

class Agenda:
    __contatos: list[Contato] = []
    __eventos: list[Evento] = []

    def __init__(self, item=None):
        if item is None:
            return
        if isinstance(item, Contato):
            Agenda.__contatos.append(item)
        elif isinstance(item, Evento):
            Agenda.__eventos.append(item)

    @staticmethod
    def contatos() -> list[Contato]:
        return list(Agenda.__contatos)

    @staticmethod
    def eventos() -> list[Evento]:
        return list(Agenda.__eventos)
