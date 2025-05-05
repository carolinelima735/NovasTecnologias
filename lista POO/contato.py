# contato.py

import datetime

class Contato:
    __slots__ = ('_nome', '_telefone', '_datanasc', '_email')

    def __init__(self, nome: str, telefone: str, datanasc: datetime.date, email: str):
        self.nome = nome
        self.telefone = telefone
        self.datanasc = datanasc
        self.email = email

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, valor: str):
        if not valor:
            raise ValueError("Nome não pode ser vazio")
        self._nome = valor

    @property
    def telefone(self) -> str:
        return self._telefone

    @telefone.setter
    def telefone(self, valor: str):
        if not valor:
            raise ValueError("Telefone não pode ser vazio")
        self._telefone = valor

    @property
    def datanasc(self) -> datetime.date:
        return self._datanasc

    @datanasc.setter
    def datanasc(self, valor: datetime.date):
        if not isinstance(valor, datetime.date):
            raise TypeError("Data de nascimento deve ser um datetime.date")
        self._datanasc = valor

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, valor: str):
        if '@' not in valor:
            raise ValueError("Email inválido")
        self._email = valor

    def __str__(self) -> str:
        data_fmt = self._datanasc.strftime('%d/%m/%Y')
        return f"{self._nome}\n{self._telefone}\n{data_fmt}\n{self._email}"
