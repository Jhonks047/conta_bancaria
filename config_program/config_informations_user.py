import string
import random
from config_program.config import color
import requests
from config_program.main_text import *


DATABASE = "https://conta-bancaria-mkl-default-rtdb.firebaseio.com/"


def get_database_info(name, sit=""):
    if sit == "bitcoin":
        new_database = DATABASE + ".json"
        info_bitcoin_user = requests.get(new_database) #    Pega as informações da database
        info_bitcoin_user = info_bitcoin_user.json() #  Transforma a variável em modo leitura json
        info_bitcoin_user = info_bitcoin_user['users'][name]['dados']['investimento']['bitcoin'] # Pega apenas a informação de bitcoin do dicionário
        return info_bitcoin_user
    elif sit == "saldo_brl":
        new_database = DATABASE + ".json"
        info_balance_user = requests.get(new_database)
        info_balance_user = info_balance_user.json()
        balance = info_balance_user['users'][name]['dados']['dados_bancarios']['money']['money_BRL']
        return balance


def verificar_users():
    users = requests.get(f"{DATABASE}.json")
    if users.status_code:
        data = users.json()
        if data is not None:
            return True
        else:
            return False


def cadastrarInformacoes(name, username, user_token, user_account):
    #TODO  Dados de login
    #*--------------------
    data_login = f'{{"user_login": "{username}", "user_token": "{user_token}"}}'
    db_login = f"{DATABASE}users/{name}/dados/login/.json"
    user_login = requests.patch(db_login, data=data_login)
    if user_login:
        print("Dados de login criados com sucesso!")
    #*--------------------
    
    #TODO  Dados bancários
    #*--------------------
    db_dados_bancarios = f"{DATABASE}users/{name}/dados/dados_bancarios/.json"
    data_dados_bancarios = f'{{"user_account": "{user_account}"}}'
    dados_bancarios = requests.patch(db_dados_bancarios, data=data_dados_bancarios)
    if dados_bancarios:
        print("Dados Bancários criados com sucesso!")
    #*--------------------
    
    #TODO   Dados Monetários
    #*--------------------
    db_dados_monetarios = f"{DATABASE}users/{name}/dados/dados_bancarios/money/.json"
    data_dados_monetarios = f'{{"money_BRL": 0}}'
    dados_monetarios = requests.patch(db_dados_monetarios, data=data_dados_monetarios)
    if dados_monetarios:
        print("Dados monetários criados com sucesso!")
    #*--------------------
    
    #TODO   Dados Investimentos
    #*--------------------
    db_dados_investimentos = f"{DATABASE}users/{name}/dados/investimentos/criptomoedas/.json"
    data_dados_investimentos = f'{{"bitcoin": 0}}'
    dados_investimentos = requests.patch(db_dados_investimentos, data=data_dados_investimentos)
    if dados_investimentos:
        print("Dados de Investimentos criados com sucesso!")
    #*--------------------
    return True

def gerarUser(name):
    prefix = name[:3].lower()
    allowed = string.ascii_lowercase+string.digits
    suffix = "".join(random.choices(allowed, k=3))
    user_name = prefix+suffix
    return user_name


def gerarToken():
    allowed = string.ascii_lowercase+string.digits
    password = "".join(random.choices(allowed, k=3))
    return password


def gerarNumeroConta():
    allowed = string.digits
    num = "".join(random.choices(allowed, k=12))
    num = f"{num[:3]}.{num[3:7]}.{num[7:10]}-{num[10:]}"
    return num


def login_user(sit=""):
    if sit == "login":
        login = str(input("Digite o user_login: ")).strip()
        return login
    elif sit == "token":
        token = str(input("Digite o token de acesso: ")).strip()
        return token


def validarLogin():
    total_de_tentativas = 3
    while total_de_tentativas > 0:
        name = str(input("Digite seu nome: ")).strip().capitalize()
        user_login = login_user("login")
        user_token = login_user("token")
        db = f"{DATABASE}.json"
        dados = requests.get(db)
        validate = dados.json()
        try:
            validate_login = validate['users'][name]['dados']['login']['user_login']
            validate_token = validate['users'][name]['dados']['login']['user_token']
            if user_login == validate_login and user_token == validate_token:
                return True, name
            else:
                total_de_tentativas -= 1
                if total_de_tentativas > 0:
                    print(f"{color('ERRO! ', 'red')}{color(f'Dados incorretos. Você tem mais {total_de_tentativas} tentativas, Tente novamente.', 'lred')}")
                else:
                    print(f"{color('Excedeu o número máximo de tentativas! Bloqueando acesso...', 'lred')}")
                    return False
        except KeyError as error:
            print(f"{color('Dados do usuário: ', 'blue')}{color(error, 'lcyan')}{color(' Não encontrados!', 'red')}")