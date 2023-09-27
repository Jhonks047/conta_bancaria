from firebase_admin import db

from config.informations_user import *
from config.main_text import *


def atualizar_balance(USER: str, amount: float=0, sit: str=""):
    """Atualizar o saldo dentro do programa ao qual foi chamado.

    Args:
        USER ( STR ): Usuário atual logado no sistema
        amount ( INT, OPTIONAL): Usado para definir quanto irá aumentar ou diminuir do saldo. Padrão 0 para nem sempre precisar informar.
        sit (STR, OPTIONAL): Usado para definir se será adicionado ou removido do saldo o valor do amount. Padrão "" para nem sempre precisar informar..
    - sit = "add": Adicionar saldo
    - sit = "rem": Remover saldo
    - sit = "num": Mostrar saldo atual

    Returns:
        FLOAT: Retorna o saldo atual do usuário.
    """
    try:
        user_ref = db.reference(f'users/{USER}/dados/dados_bancarios/dados_monetarios')
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
        elif sit == "num":
            return saldo_atual


#!  Mostrar saldo disponivel
def actual_balance_str(USER: str):
    """Formata o saldo atual em string para mostrar corretamente o valor monetário.
    Args:
        USER ( STR ): Usuário atual logado no sistema
    Returns:
        STR: Retorna a frase SALDO DISPONÍVEL junto ao saldo ja formatado para a região pt-BR
    """
    print()
    import locale
    locale.setlocale(locale.LC_ALL, 'pt-BR')
    balance_actual = atualizar_balance(USER, sit="num")
    balance_actual = round(balance_actual, 2)
    balance_actual_str = locale.format_string("%.2f", balance_actual, grouping=True)
    actual_balance = f"{color('Saldo disponível: R$ ','lgreen')}{color(balance_actual_str, 'lwhite')}"
    print(actual_balance)