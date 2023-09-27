import requests

import main
import tools.extras.investimentos.criptomoedas.main_criptomoedas
from config.get_informations import *
from config.informations_user import *
from config.main_balance import *
from config.main_text import *

def users_ref(USER, amount=0, sit=""):
    try:
        user_ref = db.reference(f'users/{USER}/dados/dados_investimento/criptomoedas')
        bitcoin_atual_usuario = user_ref.child('bitcoin').get()
    except Exception:
        print("Erro ao pegar dados de bitcoin")
    else:
        if sit == "add":
            novo_bitcoin = bitcoin_atual_usuario + amount
            user_ref.update({f'bitcoin': novo_bitcoin})
        elif sit == "rem":
            novo_bitcoin = bitcoin_atual_usuario - amount
            user_ref.update({'bitcoin': novo_bitcoin})
        elif sit == "user":
            return bitcoin_atual_usuario


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
    titulos(msg="CENTRAL DO BITCOIN", cor="lyellow")
    print(f"{color('Valor atual do bitcoin:', 'lyellow')} {get_bitcoin_price()}")
    main.actual_balance_str(USER=USER)
    print(f"{color('Meus bitcoins: ', 'cyan')}{color(get_bitcoin_user(USER=USER), 'lyellow')} | {formated_money(value=get_bitcoin_user(USER=USER) * get_bitcoin_price(sit='num'))} ")
    print(f"""
        {color("[ A ] Comprar em reais", "lyellow")}
        {color("[ B ] Comprar por unidades/fracionado", "lgreen")}
        {color("[ C ] Vender bitcoins", 'lmagenta')}
        
    {color("[ X ] Voltar", "lred")}
    """)
    opcao = choices("A", "B", "C", "X")
    if opcao == "A":
        bitcoin_brl(USER=USER)
    elif opcao == "B":
        bitcoin_fracionado(USER=USER)
    elif opcao == "C":
        vender_bitcoin(USER=USER)
    elif opcao == "X":
        tools.extras.investimentos.criptomoedas.main_criptomoedas.main_criptomoedas(USER=USER)


#   COMPRAR BITCOIN EM REAIS
def bitcoin_brl(USER):
    titulos(msg="COMPRA DE BITCOINS EM REAL", cor="lyellow")
    while True:
        try:
            saldo_atual = atualizar_balance(USER=USER, sit="num")
            valor_bitcoin = str(input("Digite aqui quantos reais gostaria de comprar em bitcoins: ")).replace(",", ".").strip()
            valor_bitcoin = float(valor_bitcoin)
            if valor_bitcoin > saldo_atual:
                raise ValueError(f"{color('Saldo insuficiente para a compra.', 'lred')}")
            elif valor_bitcoin < 15:
                raise ValueError(f"{color('Valor mínimo da compra é de: ', 'lred')}{formated_money(value=15)}")
        except ValueError as error:
            print(f"{color('ERRO! Valor inválido, tente novamente: ', 'lred')}{error}")
        else:
            total_bitcoins = valor_bitcoin / get_bitcoin_price(sit="num")
            break
    print(f"""
    {color("Sua compra ficou no valor de ", "lblue")}{formated_money(value=valor_bitcoin)}
    {color("Você está comprando ", "lblue")}{color(total_bitcoins, 'lyellow')}{color(' BITCOINS', "lblue")}""")
    opcao = options_SN()
    if opcao == "S":
        try:
            bitcoin_usuario = users_ref(USER=USER, sit="num")
        except Exception as error:
            print(f"Erro ao pegar as informações de bitcoins: {error}")
        else:
            try:
                novo_bitcoin = bitcoin_usuario + total_bitcoins
                users_ref(USER=USER, amount=novo_bitcoin, sit="add")
            except Exception as error:
                print(f"Não foi possivel adicionar dados de bitcoin ao banco de dados: {error}")
            else:
                atualizar_balance(USER=USER,amount=valor_bitcoin, sit="rem")
                bitcoin(USER=USER)
    elif opcao == "N":
        bitcoin_brl(USER=USER)


#   COMPRAR BITCOIN FRACIONADO
def bitcoin_fracionado(USER):
    titulos(msg="COMPRA DE BITCOIN POR UNIDADE | FRACIONADO", cor="lyellow")
    while True:
        try:
            saldo_atual = atualizar_balance(USER=USER, sit="num")
            quantidade_bitcoin = str(input("Digite aqui quantos bitcoins você quer comprar: ")).replace(",", ".").strip()
            quantidade_bitcoin = float(quantidade_bitcoin)
            valor_compra_bitcoin_fracionado = quantidade_bitcoin * get_bitcoin_price(sit="num")
            if valor_compra_bitcoin_fracionado > saldo_atual:
                raise ValueError(f"{color('Saldo insuficiente para a compra.', 'lred')}")
            elif valor_compra_bitcoin_fracionado < 15:
                raise ValueError(f"{color('Valor mínimo da compra é de: ', 'lred')}{formated_money(value=15)}")
        except ValueError as error:
            print(f"{color('Erro! Valor inválido, tente novamente: ', 'lred')}{error}")
        else:
            break
    print(f"""
    {color("Sua compra ficou no valor de ", "lblue")}{formated_money(value=valor_compra_bitcoin_fracionado)}
    {color("Você está comprando ", "lblue")}{color(quantidade_bitcoin, "lyellow")}{color(" BITCOINS", "lblue")}""")
    opcao = options_SN()
    if opcao == "S":
        try:
            users_ref = db.reference(f'users/{USER}/dados/dados_investimento/criptomoedas')
            bitcoin_usuario_atual = users_ref.child('bitcoin').get()
        except Exception as error:
            print(f"Erro ao pegar as informações de bitcoins: {error}")
        else:
            atualizar_balance(USER=USER, amount=valor_compra_bitcoin_fracionado, sit="rem")
            novo_bitcoin = bitcoin_usuario_atual + quantidade_bitcoin
            users_ref.update({'bitcoin': novo_bitcoin})
            bitcoin(USER=USER)
    elif opcao == "N":
        bitcoin_fracionado(USER=USER)


#   VENDER BITCOIN
def vender_bitcoin(USER):
    titulos(msg="VENDA DE BITCOINS", cor="lyellow")
    print(f"""
    {color("Você pode escolher alguma das opções abaixo para vender seus bitcoins.", sit="lcyan")}
        
        {color("[ A ] Vender por unidade/fracionado.", "lyellow")}
        {color("[ B ] Vender tudo.", "lred")}
    
    {color("[ X ] Voltar", "red")}
    """)
    opcao = choices("A", "B", "X")

    #   VENDER POR UNIDADE
    if opcao == "A":
        titulos(msg="VENDA DE BITCOINS | UNIDADE/FRACIONADO", cor="lyellow")
        while True:
            venda_unidade = float(input(color("[ Digite quantas unidades deseja vender ]: ", "lwhite")))
            valor_venda_unidade = venda_unidade * get_bitcoin_price(sit="num")
            bitcoin_usuario = users_ref(USER=USER, sit="user")
            if venda_unidade > bitcoin_usuario:
                print(color("Você não tem bitcoins suficientes para venda.", "lred"))
                continue
            else:
                print(f"""
    {color("Sua venda ficou no valor total de ", "lblue")}{formated_money(value=valor_venda_unidade)}
    {color("Você está vendendo: ", "lcyan")}{color(venda_unidade, "lwhite")}{color(" Bitcoin(s)", "lyellow")}""")
                opcao = options_SN()
                if opcao == "S":
                    try:
                        atualizar_balance(USER=USER, amount=valor_venda_unidade, sit="add")
                        novo_bitcoin = bitcoin_usuario - venda_unidade
                        users_ref(USER=USER, amount=novo_bitcoin, sit="add")
                    except Exception as error:
                        print(f"Erro ao salvar dados de bitcoins no banco de dados: {error}")
                    else:
                        bitcoin(USER=USER)
                elif opcao == "N":
                    vender_bitcoin(USER=USER)

    #   VENDER TUDO
    elif opcao == "B":
        bitcoin_usuario = users_ref(USER=USER, sit="user")
        if bitcoin_usuario <= 0:
            print(f"Você não tem nenhum bitcoin para vender, voltando ao menu anterior...")
        else:
            titulos(msg="VENDA DE BITCOINS | VENDER TUDO", cor="lred")
            valor_venda_tudo = bitcoin_usuario * get_bitcoin_price(sit="num")
            print(f"""
        {color("Sua venda ficou no valor total de ", "lblue")}{formated_money(value=valor_venda_tudo)}
        {color("Você está vendendo todos os seus bitcoins", "lcyan")}""")
            opcao = options_SN()
            if opcao == "S":
                try:
                    users_ref(USER=USER, amount=bitcoin_usuario, sit="rem")
                except Exception as error:
                    print(f"Erro ao salvar dados de bitcoins no banco de dados: {error}")
                else:
                    atualizar_balance(USER=USER, amount=valor_venda_tudo, sit="add")
                    bitcoin(USER=USER)
            elif opcao == "N":
                vender_bitcoin(USER=USER)