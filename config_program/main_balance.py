from config_program.config_informations_user import cadastrarMoney

def update_balance(amount=0, sit=""):
    """Atualizar o saldo dentro do programa ao qual foi chamado.

    Args:
        amount (int, optional): Usado para definir quanto irá aumentar ou diminuir do saldo. Padrão 0 para nem sempre precisar informar.
        sit (str, optional): Usado para definir se será adicionado ou removido do saldo o valor do amount. Padrão "" para nem sempre precisar informar..
        sit = "add": Adicionar saldo
        sit = "rem": Remover saldo

    Returns:
        FLOAT/INT: Retornar o valor do balance já definido com aumento, ou redução.
    """
    balance = lerBalance()
    if sit == "add":
        balance += amount
    elif sit == "rem":
        balance -= amount
    cadastrarMoney(f"money_user.txt", balance)
    return balance


def lerBalance():
    try:
        with open(f"money_user.txt","r") as arquivo:
            balance = arquivo.read()
    except:
        print("Erro ao pegar o saldo!")
    else:
        balance = float(balance)
        return balance