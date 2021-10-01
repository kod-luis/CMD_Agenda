from os import system

def cabecalho(txt):
    system('cls')
    print('-=-'*15)
    print(f'{txt}'.center(45))
    print('-=-'*15)
    
def menu(opt:list):
    listamenu = opt
    escolha = 0
    cabecalho('AGENDA TEFOLONICA')
    for i, reg in enumerate(listamenu):
        print(f'[ {i+1} ] - {reg}')
    while True:
        try:
            print()
            escolha = int(input('Digite sua opção: '))
        except KeyboardInterrupt:
            print()
            print('-='*10)
            print('O usuário escolheu sair')
            escolha = 6
            break
        except:
            print('-='*10)
            print('ERRO! Opção inválida')
        else:
            break
    return escolha
