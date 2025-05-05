# main.py

import datetime
from contato import Contato
from contato_emergencia import ContatoEmergencia
from evento import Evento
from agenda import Agenda

MENU = '''
1. Criar contato
2. Editar contato
3. Listar contatos
4. Criar contato de emergência
5. Criar/listar eventos
6. Sair
Escolha uma opção: '''

def ler_data(prompt: str) -> datetime.date:
    while True:
        try:
            txt = input(prompt + ' (dd/mm/aaaa): ')
            d, m, a = map(int, txt.split('/'))
            return datetime.date(a, m, d)
        except Exception:
            print('Data inválida, tente novamente.')


def main():
    while True:
        opc = input(MENU)
        match opc:
            case '1':  # Criar contato
                nome = input('Nome: ')
                tel  = input('Telefone: ')
                dat  = ler_data('Data de nascimento')
                email= input('Email: ')
                try:
                    c = Contato(nome, tel, dat, email)
                    Agenda(c)
                    print('Contato criado!')
                except Exception as e:
                    print('Erro:', e)

            case '2':  # Editar contato
                contatos = Agenda.contatos()
                for i, c in enumerate(contatos):
                    print(f'{i}:', c.nome)
                idx = int(input('Índice do contato a editar: '))
                try:
                    c = contatos[idx]
                    c.nome = input('Novo nome: ') or c.nome
                    c.telefone = input('Novo telefone: ') or c.telefone
                    c.datanasc = ler_data('Nova data de nascimento')
                    c.email = input('Novo email: ') or c.email
                    print('Contato atualizado!')
                except Exception as e:
                    print('Erro:', e)

            case '3':  # Listar contatos
                for c in Agenda.contatos():
                    print('---')
                    print(c)

            case '4':  # Criar contato de emergência
                nome = input('Nome: ')
                tel  = input('Telefone: ')
                dat  = ler_data('Data de nascimento')
                email= input('Email: ')
                try:
                    ce = ContatoEmergencia(nome, tel, dat, email)
                    Agenda(ce)
                    print('Contato de emergência criado!')
                except Exception as e:
                    print('Erro:', e)

            case '5':  # Criar/listar eventos
                sub = input('d para criar, l para listar: ').lower()
                if sub == 'd':
                    desc = input('Descrição do evento: ')
                    di = ler_data('Data início')
                    df = ler_data('Data fim')
                    contatos = Agenda.contatos()
                    for i, c in enumerate(contatos): print(f'{i}:', c.nome)
                    ci = int(input('Índice do contato: '))
                    try:
                        ev = Evento(desc, di, df, contatos[ci])
                        Agenda(ev)
                        print('Evento criado!')
                    except Exception as e:
                        print('Erro:', e)
                elif sub == 'l':
                    for ev in Agenda.eventos():
                        print('---')
                        print(ev.get_informacoes())

            case '6':  # Sair
                total = Evento.get_total_eventos()
                print(f'Total de eventos: {total}')
                break

            case _:
                print('Opção inválida!')

if __name__ == '__main__':
    main()
