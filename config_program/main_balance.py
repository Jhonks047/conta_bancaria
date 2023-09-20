from config_program.config_informations_user import *
from firebase_admin import db


def atualizar_balance(USER, amount=0, sit=""):
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
def actual_balance_str(USER):
    """Formata o saldo atual em string para mostrar corretamente o valor monetário.

    Returns:
        STRING: Retorna a frase SALDO DISPONÍVEL junto ao saldo ja formatado para a região pt-BR
    """
    print()
    import locale
    locale.setlocale(locale.LC_ALL, 'pt-BR')
    balance_actual = atualizar_balance(USER, sit="num")
    balance_actual = round(balance_actual, 2)
    balance_actual_str = locale.format_string("%.2f", balance_actual, grouping=True)
    actual_balance = color("Saldo disponível: R$ ","lgreen")+color(balance_actual_str, "lwhite")
    print(actual_balance)


def pegar_informacoes_database(USER, sit=""):
    if sit == "conta_bancaria":
        try:
            users_ref = db.reference(f'users/{USER}/dados/dados_bancarios')
            conta_bancaria = users_ref.child('numero_da_conta').get()
        except Exception as error:
            print(f"Erro ao pegar o número da conta: {error}")
        else:
            print(f"{color('Número da conta: ', 'lcyan')}{color(conta_bancaria, 'lyellow')}")