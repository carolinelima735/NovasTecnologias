# contato_emergencia.py

from contato import Contato

class ContatoEmergencia(Contato):
    __slots__ = ('_prioridade',)

    def __init__(self, nome, telefone, datanasc, email, prioridade: bool = True):
        super().__init__(nome, telefone, datanasc, email)
        self._prioridade = prioridade

    @property
    def prioridade(self) -> bool:
        return self._prioridade

    def __str__(self) -> str:
        base = super().__str__()
        return f"{base}\nPrioridade: {self._prioridade}"  
