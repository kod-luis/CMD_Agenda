from dbuteis import *
from interface import *
from time import sleep

while True:
    opt = menu(['Adicionar Contato', 'Deletar Contato',
                'Atualizar Contato', 'Consultar ID',
                'Listar Contatos', 'Sair'])

    if opt == 1:
        cabecalho('Adicionando Contato')
        nome = str(input('Digite o nome: ')).strip().title()
        tel = str(input('Digite o telefone [(99) 99999-9999]: ')).strip()
        email = str(input('Digite o e-mail: ')).strip()
        ret = queryDB(f"INSERT INTO tb_contatos (T_NOMECONTATO,T_TELEFONECONTATO,T_EMAILCONTATO) VALUES ('{nome}','{tel}','{email}');")
        cabecalho(f'ADICIONANDO {nome}...')
        sleep(2)
        if len(ret) == 0:
            print(f'{nome} adicionado com sucesso a agenda!')
        else:
            print(f'ERRO: {ret}')
        print('-='*10)
        system('pause')
    elif opt == 2:
        cabecalho('Deletando Contato')
        while True:
            try:
                cod = int(input('Informe o código do contato que deseja deletar: '))
            except KeyboardInterrupt:
                print()
                print('-='*10)
                print('O usuário escolheu não informar!')
                break
            except:
                print('-='*10)
                print('Código inválido!')
            else:
                cabecalho(f'EXCLUINDO ...')
                ret = queryDB(f"DELETE FROM tb_contatos WHERE N_IDCONTATO = '{cod}';")
                sleep(2)
                if len(ret) == 0:
                    print('Contato deletado com sucesso!')
                else:
                    print(f'ERRO: {ret}')
                break
        print('-='*10)
        system('pause')
    elif opt == 3:
        cabecalho('Atualizando Contato')
        while True:
            try:
                cod = int(input('Informe o código do contato que deseja alterar: '))
            except KeyboardInterrupt:
                print()
                print('-='*10)
                print('O usuário escolheu não informar!')
                break
            except:
                print('-='*10)
                print('Código inválido')
            else:
                print('-='*10)
                nome = str(input('Digite o novo nome: ')).strip().title()
                tel = str(input('Digite o novo telefone [(99) 99999-9999]: ')).strip()
                email = str(input('Digite o novo e-mail: ')).strip()
                cabecalho('ATUALIZANDO...')
                ret = queryDB(f"UPDATE tb_contatos SET T_NOMECONTATO = '{nome}',T_TELEFONECONTATO = '{tel}',T_EMAILCONTATO = '{email}' WHERE N_IDCONTATO = '{cod}';")
                sleep(2)
                if len(ret) == 0:
                    print('Contato atualizado com sucesso!')
                else:
                    print(f'ERRO: {ret}')
                break
        print('-='*10)
        system('pause')
    elif opt == 4:
        cabecalho('Consultando ID')
        while True:
            try:
                cod = int(input('Informe o código do contato que deseja consultar: '))
            except KeyboardInterrupt:
                print()
                print('-='*10)
                print('O usuário escolheu não informar')
                break
            except:
                print('-='*10)
                print('Código inválido')
            else:
                cabecalho('CONSULTANDO...')
                if cod < 0:
                    query = f"SELECT * FROM tb_contatos;"
                else:
                    query = f"SELECT * FROM tb_contatos WHERE N_IDCONTATO = '{cod}';"
                ret = listDB(query)
                sleep(2)
                if len(ret[0]) == 0:
                    print(f'{"ID":>4} | {"Nome":<30} | {"Telefone":<20} | {"E-mail":<30}')
                    if len(ret[1]) > 0:
                        print(f'{str(ret[1][0][0]):>4} | {str(ret[1][0][1]):<30} | {str(ret[1][0][2]):<20} | {str(ret[1][0][3]):<30}')
                    else:
                        print(' --- Registro não encontrado')                        
                else:
                    print(f'ERRO: {ret[0]}')
                break
        print('-='*10)
        system('pause')
    elif opt == 5:
        cabecalho('CARREGANDO CONTATOS...')
        ret = listDB(f"SELECT * FROM tb_contatos;")
        sleep(2)
        cabecalho('Lista de Contatos')        
        if len(ret[0]) == 0:
            print(f'{"ID":>4} | {"Nome":<30} | {"Telefone":<20} | {"E-mail":<30}')
            if len(ret[1]) > 0:
                for reg in ret[1]:
                    print(f'{str(reg[0]):>4} | {str(reg[1]):<30} | {str(reg[2]):<20} | {str(reg[3]):<30}')
            else:
                print(' --- Registro não encontrado')                        
        else:
            print(f'ERRO: {ret[0]}')
        print('-='*10)
        system('pause')
    elif opt == 6:
        system('cls')
        print('-='*10)
        print('Saindo da agenda...')
        sleep(2)
        break
    else:
        print('-='*10)
        print('Opção não existe!')
        sleep(1)
print('-='*10)
print('Volte Sempre!')
system('pause')
