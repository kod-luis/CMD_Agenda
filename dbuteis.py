import sqlite3 as db
from sqlite3 import Error
from sqlite3.dbapi2 import Connection

def getFile(file:str, pasta:str, txt:str=''):
    """
    :param file: informe __file__
    :param pasta: pasta onde está o arquivo
    :param txt: nome do arquivo que deseja encontrar
    :return: retorna o caminho completo do arquivo informado
    """
    import os
    caminhofile = str(os.path.dirname(file))
    lugardapasta = caminhofile.find(pasta) + len(pasta)
    
    caminho = os.path.join(caminhofile[:lugardapasta],txt)
    return caminho

def conectardb(): #função para conectar ao banco de dados
    caminho = getFile(__file__,'Agenda','agenda.db') #tem que passar o caminho    
    try:
        con = db.connect(caminho) #função do sqllite para conectar
    except Error as ex:
        print(ex) #caso aconteça algum erro na conexão ele retorna aqui
        con = Connection()
        return con
    else:
        return con #retorno com a conexão

def criarTabeladb(q:str):
    query = q
    conex = conectardb()
    try:
        vcursor = conex.cursor()
        vcursor.execute(query)
    except Error as ex:
        print(f'ERRO: {ex}')
    else:
        print('Tabela criada com sucesso!')
    finally:
        conex.close()

def queryDB(q):
    query = q
    msg = ''
    conex = conectardb()
    try:
        c = conex.cursor()
        c.execute(query)
    except Error as ex:
        msg = f'ERRO: {ex}'
    else:
        conex.commit()
        msg = ''
    finally:
        conex.close()
        return msg

def listDB(q):
    query = q
    conex = conectardb()
    tabela = list()
    msg = ''
    try:
        c = conex.cursor()
        c.execute(query)
    except Error as ex:
        msg = f'ERRO: {ex}'
        tabela = [msg, []]
    else:
        tabela = [msg, c.fetchall()]
    finally:
        conex.close()
        return tabela


