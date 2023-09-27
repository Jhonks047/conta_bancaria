import firebase_admin
from firebase_admin import auth, credentials, db

from config.informations_user import *
from config.main_text import *


cred = credentials.Certificate(r"C:\Users\jhona\OneDrive\Documentos\MeusProjetos\conta_bancaria\token\conta-bancaria-mkl-firebase-adminsdk-qxtvi-b80bb839e2.json")
firebase_admin.initialize_app(cred, {'databaseURL': 'https://conta-bancaria-mkl-default-rtdb.firebaseio.com'})


def criar_usuario(email: str, senha: str, uid: str, name: str):
    """CRIAÇÃO DO USUÁRIO AO BANCO DE DADOS

    Args:
        email (str): Email gerado por outra função para adicionar ao banco de dados
        senha (str): Senha escolhida pelo usuário para autenticar o login
        uid (str): UID gerada pelo usuário para autenticar as transações bancárias
        name (str): Nome do usuário

    Returns:
        CREDENTIALS: Retorna as credenciais do user para efetuar o login
    """    
    try:
        user = auth.create_user(
            uid=uid,
            email=email,
            password=senha,
            display_name=name
            )
        print(f"""
    {color("Usuário registrado com sucesso! Seja muito bem vindo(a): ", "lgreen")}>> {color(user.display_name, "lwhite")} <<
    {color("Por favor, guarde esse UID, ele é sua única forma de login!", "lcyan")}
    {color("Sua UID: ", "yellow")}{color(user.uid, "lwhite")}
    {color("Para efetuar o login usando seu UID, basta escrever o UID junto ao @mkl.bank. Exemplo usando seu UID: ", "lcyan")}{color(user.uid, "lwhite")}{color("@mkl.bank", "lyellow")}
    """)
        return user
    except auth.EmailAlreadyExistsError:
        print(color("Um email com esse nome já existe!", "lcyan"))
        return None


def criar_informacoes(uid: str, numero_da_conta: str, name: str):
    """CRIA AS INFORMAÇÕES DENTRO DO BANCO DE DADOS

    Args:
        uid (str): UID do usuário para criar os dados no banco de dados
        numero_da_conta (str): Número da conta para salvar as informações no banco de dados
        name (str): Nome do usuário para adicionar ao banco de dados
    """

    users_ref = db.reference('users')
    
    if not users_ref.child(uid).get():
        estrutura_padrao = {
            'dados': {
                'dados_bancarios': {
                    'dados_monetarios': {
                        'money_BRL': 0.0,
                        'money_USD': 0.0
                    },
                    'numero_da_conta': numero_da_conta,
                    'display_name': name
                },
                'dados_investimento': {
                    'criptomoedas': {
                        'bitcoin': 0.0,
                        'ethereum': 0.0
                    }
                }
            }
        }
        users_ref.child(uid).set(estrutura_padrao)


def fazer_login():
    """REALIZAR O LOGIN DO USUÁRIO AUTENTICANDO NO BANCO DE DADOS

    Returns:
        CREDENTIALS: Retorna as credenciais do usuário para autenticar o login em outra função
    """
    titulos(msg="ÁREA DE LOGIN", cor="yellow")
    print(color("Olá! Bem vindo de volta, para efetuar seu login, basta informar suas credenciais abaixo.", "lcyan"))
    print()
    user_email = str(input("Digite seu login <Seu UID + @mkl.bank>: ")).strip().lower()
    user_password = str(input("Digite sua senha: ")).strip()
    try:
        user = auth.get_user_by_email(user_email)
        user = auth.update_user(
            user.uid,
            email=user_email,
            password=user_password
        )
        print(f"Usuário logado com o ID: {user.uid}@mkl.bank")
        return user
    except auth.UserNotFoundError:
        print("O usuário não foi encontrado!")
        return None
    except auth.EmailNotFoundError:
        print("Não existe nenhum email cadastrado!")
        return None
    except ValueError:
        print(color("Email e/ou senha inválidos! Tente novamente.", "lred"))
        return None
    