import requests

import main
import tools.extras.investimentos.criptomoedas.main_criptomoedas
from config.get_informations import *
from config.informations_user import *
from config.main_balance import *
from config.main_text import *


def get_bitcoin_user(USER):
    bitcoins = pegar_informacoes_database(USER=USER, sit="bitcoins")
    return bitcoins


def get_bitcoin_price(sit="str"):
    api = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=brl"
    bitcoin_price_api = requests.get(api)
    bitcoin_price = bitcoin_price_api.json()
    bitcoin_price = bitcoin_price['bitcoin']['brl']
    if sit == "str":
        return formated_money(bitcoin_price)
    elif sit == "num":
        return bitcoin_price


def bitcoin(USER):
    titulos("CENTRAL DO BITCOIN")
    print(f"{color('Valor atual do bitcoin:', 'lyellow')} {get_bitcoin_price()}")
    main.actual_balance_str(USER=USER)
    print(f"{color('Total de bitcoins:', 'cyan')}{get_bitcoin_user(USER=USER)} | {color('Total em reais:', 'blue')}{formated_money(value=get_bitcoin_user(USER=USER) * get_bitcoin_price(sit='num'))} ")
    print(f"""
        {color("[ A ] Comprar por real", "lyellow")}
        {color("[ B ] Comprar por unidades", "lgreen")}
        {color("[ C ] Vender bitcoins", 'lmagenta')}
        
    {color("[ X ] Voltar", "lred")}""")
    option = choices("A", "B", "X")
    if option == "A":
        bitcoin_brl(USER=USER)
    elif option == "B":
        pass
    elif option == "C":
        pass
    elif option == "X":
        tools.extras.investimentos.criptomoedas.main_criptomoedas.main_criptomoedas(USER=USER)


def bitcoin_brl(USER):
    titulos("COMPRA DE BITCOINS EM REAL")
    valor_bitcoin = float(input("Digite aqui quantos reais gostaria de comprar em bitcoins: "))
    total_bitcoins = valor_bitcoin / get_bitcoin_price(sit="num")
    print(f"""
    {color('Sua compra ficou no valor de ', 'lblue')}{formated_money(value=valor_bitcoin)}
    {color('Você está comprando ', 'lblue')}{color(total_bitcoins, 'lyellow')}{' BITCOINS'}""")
    option = options_SN()
    if option == "S":
        try:
            users_ref = db.reference(f'users/{USER}/dados/dados_investimento/criptomoedas')
            bitcoin_usuario_atual = users_ref.child('bitcoin').get()
        except Exception as error:
            print(f"Erro ao pegar as informações de bitcoins: {error}")
        else:
            atualizar_balance(USER=USER,amount=valor_bitcoin, sit="rem")
            novo_bitcoin = bitcoin_usuario_atual + total_bitcoins
            users_ref.update({'bitcoin': novo_bitcoin})
            bitcoin(USER=USER)