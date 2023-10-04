###################################################################################################

#TODO                           imports da pasta do programa

from config.get_informations import *
from config.main_balance import *
from config.main_text import *

###################################################################################################


#  Função do depósito
def deposito(USER):
    """Depósito bancário
        Essa função efetua o depósito para o usuário, definido o valor pelo qnt_balance que começa com o tipo str para poder trocar
        a ( , ) pelo ( . ) para transformar em float
    Raises:
        ValueError = Depósito igual a 0: Impedir que o usuário deposite um valor 0.
        ValueError = Depósito com valor negativo: Impedir que o usuário deposite com um valor negativo.

    Returns:
        FLOAT: Retorna o valor do depósito definido pelo usuário para adicionar o saldo a conta do usuário no menu principal.
    """

    titulos(msg="ÁREA DE DEPÓSITO", cor="lgreen")
    print(f"""
    {color("Aqui você realiza seus depósitos para usar os ", "lcyan")}
    {color("serviços bancários, incluindo investimentos e ", "lcyan")}
    {color("apostas na área das loterias entre outras transações.", "lcyan")}
    """)
    while True:
        try:
            valor_deposito = str(input(color("Digite o valor que deseja depositar R$: ", "lwhite"))).replace(",", ".").strip()
            valor_deposito = float(valor_deposito)
            if valor_deposito == 0:
                raise ValueError(f"Você não pode depositar {formated_money(value=0)}!")
            elif valor_deposito < 0:
                raise ValueError(f"Você não pode depositar um valor negativo!")
        except ValueError as error:
            print(color(f"Erro: {error}","red"))
        else:
            loading(10, "Registrando depósito.")
            print(f"{'Você irá depositar: '}{formated_money(valor_deposito)}")
            confirm = options_SN()
            if confirm == "S":
                atualizar_balance(USER=USER, amount=valor_deposito, sit="add")
                print(color("Deposito feito com sucesso!","lgreen"))
                break
            else:
                loading(20, "Voltando a opção anterior.")
                continue


#  Função do saque
def transferencia(USER):
    """Saque bancário.
        Essa função efetua a transferencia para o usuário, definido o valor pelo <valor_transferencia> que começa com o tipo str para poder trocar ( , ) pelo ( . ) para transformar em float
    Raises:
        ValueError = Saque igual a 0: Impedir que o usuário saque um valor 0.
        ValueError = Saque com valor negativo: Impedir que o usuário saque com um valor negativo.

    Returns:
        FLOAT: Retorna o valor do saque definido pelo usuário para remover o saldo a conta do usuário no menu principal.
    """

    titulos(msg="ÁREA DE TRANSFERÊNCIA", cor="lred")
    print(f"""
        {color("Aqui você transfere dinheiro da sua conta ", "lcyan")}
        {color("para outra pessoa ou instituição.", "lcyan")}""")
    while True:
        try:
            valor_transferencia = str(input("Digite o valor que deseja transferir R$: ")).replace(",", ".").strip()
            valor_transferencia = float(valor_transferencia)
            if valor_transferencia == 0:
                raise ValueError(f"Você não pode transferir {formated_money(0)}!")
            elif valor_transferencia < 0:
                raise ValueError(f"Você não pode transferir um valor negativo!")
            elif valor_transferencia > atualizar_balance(USER, sit="num"):
                raise ValueError(f"Você não pode transferir um valor acima do seu saldo!")
        except ValueError as error:
            print(color(f"Erro: {error}","red"))
            return None
        else:
            #*  Definir aqui a pessoa que irá receber a transferência
            confirm = options_SN()
            if confirm == "S":
                break
            else:
                loading(20, "Voltando a opção anterior.")
                continue