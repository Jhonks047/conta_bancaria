import string
import random
from config_program.config import color
import requests
from config_program.main_text import *


DATABASE = "https://conta-bancaria-mkl-default-rtdb.firebaseio.com/"


def get_database_info(sit=""):
    pass


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
    #!--------------------
    data_login = f'{{"user_login": "{username}", "user_token": "{user_token}"}}'
    db_login = f"{DATABASE}users/{name}/dados/login/.json"
    user_login = requests.patch(db_login, data=data_login)
    
    #TODO  Dados bancários
    #!--------------------
    db_dados_bancarios = f"{DATABASE}users/{name}/dados/dados_bancarios.json"
    data_dados_bancarios = f'{{"user_account": "{user_account}"}}'
    dados_bancarios = requests.patch(db_dados_bancarios, data=data_dados_bancarios)
    #!--------------------
    
    #!  Verificar o salvamento de dados da databse
    if user_login and dados_bancarios:
        print(color("Dados salvos com sucesso!", "lgreen"))
        return True
    else:
        return False

def cadastrarMoney(money):
    try:
        data = f'{{"money_BRL": {money}}}'
        pass
    except Exception as error:
        print(f"Houve um erro ao salvar o dinheiro! {error}")


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
                return True
            else:
                total_de_tentativas -= 1
                if total_de_tentativas > 0:
                    print(f"{color('ERRO! ', 'red')}{color(f'Dados incorretos. Você tem mais {total_de_tentativas} tentativas, Tente novamente.', 'lred')}")
                else:
                    print(f"{color('Excedeu o número máximo de tentativas! Bloqueando acesso...', 'lred')}")
                    return False
        except KeyError as error:
            print(f"{color('Dados do usuário: ', 'blue')}{color(error, 'lcyan')}{color(' Não encontrados!', 'red')}")