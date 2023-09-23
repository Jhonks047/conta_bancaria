import firebase_admin
from firebase_admin import auth, credentials, db

from config.informations_user import *
from config.main_text import *

cred = credentials.Certificate(r"C:\Users\jhona\OneDrive\Documentos\MeusProjetos\conta_bancaria\token\conta-bancaria-mkl-firebase-adminsdk-qxtvi-b80bb839e2.json")
firebase_admin.initialize_app(cred, {'databaseURL': 'https://conta-bancaria-mkl-default-rtdb.firebaseio.com'})

def criar_usuario(email, senha, uid, name):
    try:
        user = auth.create_user(
            uid=uid,
            email=email,
            password=senha,
            display_name=name
            )
        print(f"Usuário criado com o ID: {user.uid}")
        return user
    except auth.EmailAlreadyExistsError:
        print(color("Erro ao criar um usuário com esse nome!", "lred"))
        print(color("Um email com esse nome já existe!", "lcyan"))
        return None


def criar_informacoes(uid, numero_da_conta, name):
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
    titulos("ÁREA DE LOGIN")
    user_email = str(input("Digite seu email, incluindo o <@mkl.bank>: ")).strip().lower()
    user_password = str(input("Digite sua senha: ")).strip()
    try:
        user = auth.get_user_by_email(user_email)
        user = auth.update_user(
            user.uid,
            email=user_email,
            password=user_password
        )
        print(f"Usuário logado com o ID: {user.uid}")
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
    