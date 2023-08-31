import string
import random
from config_program.config import color_bright
import config_program.main_text


def criarArquivo(name):
    try:
        with open(name, "r") as arquivo:
            arquivo.read()
    except FileNotFoundError:
        return False
    else:
        return True


def cadastrarInformacoes(name_file, username, user_token, user_account, money=0):
    try:
        with open(name_file, "a") as arquivo:
            arquivo.write(f"Username: {username}\nToken: {user_token}\nAccount number: {user_account}")
    except:
        print("Houve um erro na abertura do arquivo!")


def cadastrarMoney(name_file, money):
    money = str(money)
    try:
        with open(name_file, "w") as arquivo:
            arquivo.write(money)
    except Exception as e:
        print(f"Houve um erro ao salvar o dinheiro! {e}")


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


def login_user():
    tentativas = 3
    while True:
        user_login = str(input("Digite o user_login: "))
        user_token_login = str(input("Digite o token de acesso: "))
        if validarLogin(user_login, user_token_login):
            return True
        else:
            tentativas -= 1
            print(color_bright(f"Usuário/senha inválidos! Apenas mais [ {tentativas} ] tentativas!","r"))
            if tentativas == 0:
                return False


def validarLogin(username, token):
    with open(f"user_info.txt","r") as arquivo:
        validate = arquivo.readlines()

    username_validate = validate[0][10:16]
    token_validate = validate[1][7:10]
    
    validarDados = False
    
    if username_validate == username and token_validate == token:
        validarDados = True
    if validarDados:
        config_program.main_text.titulos(f"ACESSO PERMITIDO")
        return True
    else:
        return False