from config_program.main_text import *
from config_program.config import *
from config_program.config_informations_user import *
import main
import requests



def get_bitcoin_user(buyed_bitcoins=0):
    bitcoin_user = requests.get(DATABASE)
    bitcoin_user = bitcoin_user.json()
    if 'bitcoins' in bitcoin_user:
        bitcoin_user = bitcoin_user['bitcoins']
        bitcoin_user += buyed_bitcoins
        return bitcoin_user
    else:
        return False


def get_bitcoin_price(sit="str"):
    api = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=brl"
    bitcoin_price_api = requests.get(api)
    bitcoin_price = bitcoin_price_api.json()
    bitcoin_price = bitcoin_price['bitcoin']['brl']
    if sit == "str":
        return formated_money(bitcoin_price)
    elif sit == "num":
        return bitcoin_price


def bitcoin():
    titulos("CENTRAL DO BITCOIN")
    print(f"{color('Valor atual do bitcoin:', 'lyellow')} {get_bitcoin_price()}")
    print(main.actual_balance_str())
    print(f"{color('Total de bitcoins:', 'cyan')} | {color('Total em reais:', 'blue')} ")
    print(f"""
        {color("[ A ] Comprar por real", "lyellow")}
        {color("[ B ] Comprar por unidades", "lgreen")}
        
    {color("[ X ] Voltar", "lred")}""")
    option = choices("A", "B", "X")
    if option == "A":
        bitcoin_real()


def bitcoin_real():
    titulos("COMPRA DE BITCOINS EM REAL")
    valor_bitcoin = float(input("Digite aqui quantos reais gostaria de comprar em bitcoins: "))
    total_bitcoins = valor_bitcoin / get_bitcoin_price(sit="num")
    option = options_SN(f"Você está comprando {total_bitcoins} bitcoins, deseja confirmar? [ S / N ]")
    if option == "S":
        if not get_bitcoin_user():
            data = f'{{"bitcoins": {total_bitcoins}}}'
            status = requests.patch(db, data=data)
        else:
            data = f'{{"bitcoins": {get_bitcoin_user(total_bitcoins)}}}'
            status = requests.patch(db, data=data)
        if status:
            print(color("Dados salvos com sucesso!", "lgreen"))
        else:
            print(color("Os dados não foram salvos. ERRO!", "lred"))