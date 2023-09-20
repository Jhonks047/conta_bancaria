from config_program.config_informations_user import *
from firebase_admin import db


def atualizar_balance(user, amount, sit=""):
    """Atualizar o saldo dentro do programa ao qual foi chamado.

    Args:
        amount (int, optional): Usado para definir quanto irá aumentar ou diminuir do saldo. Padrão 0 para nem sempre precisar informar.
        sit (str, optional): Usado para definir se será adicionado ou removido do saldo o valor do amount. Padrão "" para nem sempre precisar informar..
        sit = "add": Adicionar saldo
        sit = "rem": Remover saldo

    Returns:
        FLOAT/INT: Retornar o valor do balance já definido com aumento, ou redução.
    """
    try:
        user_ref = db.reference(f'users/{user}/dados/dados_bancarios/dados_monetarios')
        saldo_atual = user_ref.child('money_BRL').get()
    except Exception as error:
        print(f"Erro ao pegar o saldo atual {error}")
    else:
        if sit == "add":
            novo_saldo = saldo_atual + amount
            user_ref.update({'money_BRL': novo_saldo})
        elif sit == "rem":
            novo_saldo = saldo_atual - amount
            user_ref.update({'money_BRL': novo_saldo})