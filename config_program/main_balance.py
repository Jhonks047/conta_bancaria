from config_program.config_informations_user import *

def update_balance(USER, amount=0, sit=""):
    """Atualizar o saldo dentro do programa ao qual foi chamado.

    Args:
        amount (int, optional): Usado para definir quanto irá aumentar ou diminuir do saldo. Padrão 0 para nem sempre precisar informar.
        sit (str, optional): Usado para definir se será adicionado ou removido do saldo o valor do amount. Padrão "" para nem sempre precisar informar..
        sit = "add": Adicionar saldo
        sit = "rem": Remover saldo

    Returns:
        FLOAT/INT: Retornar o valor do balance já definido com aumento, ou redução.
    """
    balance = get_database_info(USER, sit="saldo_brl")
    if sit == "add":
        balance += amount
    elif sit == "rem":
        balance -= amount
    return balance
