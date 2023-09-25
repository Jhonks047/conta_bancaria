###################################################################################################

#TODO                           imports da pasta do programa

from config.get_informations import *
from config.main_balance import *
from config.main_text import *

###################################################################################################


#!  Função do depósito
def deposit():
    """Depósito bancário

    Raises:
        ValueError = Depósito igual a 0: Impedir que o usuário deposite um valor 0.
        ValueError = Depósito com valor negativo: Impedir que o usuário deposite com um valor negativo.

    Returns:
        FLOAT: Retorna o valor do depósito definido pelo usuário
    """
    titulos(msg="ÁREA DE DEPÓSITO", cor="lgreen")
    print(f"""
    {color("Aqui você realiza seus depósitos para usar os ", "lcyan")}
    {color("serviços bancários, incluindo investimentos e ", "lcyan")}
    {color("apostas na área das loterias entre outras transações.", "lcyan")}
    """)
    while True:
        try:
            qnt_balance = str(input(color("Digite o valor que deseja depositar R$: ", "lwhite"))).replace(",", ".").strip()
            qnt_balance = float(qnt_balance)
            if qnt_balance == 0:
                raise ValueError(f"Você não pode depositar {formated_money(value=0)}!")
            elif qnt_balance < 0:
                raise ValueError(f"Você não pode depositar um valor negativo!")
        except ValueError as error:
            print(color(f"Erro: {error}","red"))
        else:
            loading(10, "Registrando depósito.")
            print(f"{'Você irá depositar: '}{formated_money(qnt_balance)}")
            confirm = options_SN()
            if confirm == "S":
                break
            else:
                loading(20, "Voltando a opção anterior.")
                continue
    return qnt_balance


#!  Função do saque
def withdraw(USER):
    """Saque bancário.

    Raises:
        ValueError = Saque igual a 0: Impedir que o usuário saque um valor 0.
        ValueError = Saque com valor negativo: Impedir que o usuário saque com um valor negativo.

    Returns:
        FLOAT: Retorna o valor do saque definido pelo usuário
    """
    titulos(msg="ÁREA DE TRANSFERÊNCIA", cor="lred")
    print(f"""
        {color("Aqui você transfere dinheiro da sua conta ", "lcyan")}
        {color("para outra pessoa ou instituição.", "lcyan")}""")
    while True:
        try:
            qnt_withdraw = str(input("Digite o valor que deseja transferir R$: ")).replace(",", ".").strip()
            qnt_withdraw = float(qnt_withdraw)
            if qnt_withdraw == 0:
                raise ValueError(f"Você não pode sacar {formated_money(0)}!")
            elif qnt_withdraw < 0:
                raise ValueError(f"Você não pode sacar um valor negativo!")
            elif qnt_withdraw > atualizar_balance(USER, sit="num"):
                raise ValueError(f"Você não pode sacar um valor acima do seu saldo!")
            loading(10, "Registrando saque.")
        except ValueError as error:
            print(color(f"Erro: {error}","red"))
            return None
        else:
            print(f"{'Você irá sacar: '}{formated_money(qnt_withdraw)}")
            confirm = options_SN()
            if confirm == "S":
                break
            else:
                loading(20, "Voltando a opção anterior.")
                continue
    return qnt_withdraw