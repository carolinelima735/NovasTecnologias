# evento.py

import datetime
from contato import Contato

class Evento:
    __total_eventos = 0

    def __init__(self, descricao: str, data_inicio: datetime.date, data_fim: datetime.date, contato: Contato):
        self.descricao = descricao
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.contato = contato
        Evento.__total_eventos += 1

    def get_informacoes(self) -> str:
        di = self.data_inicio.strftime('%d/%m/%Y')
        df = self.data_fim.strftime('%d/%m/%Y')
        return (f"Descrição: {self.descricao}\n"
                f"Início : {di}\n"
                f"Fim    : {df}\n"
                f"Contato: {self.contato.nome}")

    @staticmethod
    def get_total_eventos() -> int:
        return Evento.__total_eventos
