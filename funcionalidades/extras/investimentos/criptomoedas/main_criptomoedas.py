from config_program.main_text import *
from config_program.config import *
import funcionalidades.extras.investimentos.main_investimentos
import funcionalidades.extras.investimentos.criptomoedas.bitcoin.main_bitcoin
def main_criptomoedas(USER):
    print()
    titulos("MENU DAS CRIPTOMOEDAS")
    print()
    print(f"""
        {color("[ A ] Bitcoin", "lyellow")}
        
    {color("[ X ] Voltar", "lred")}""")
    option = choices("A", "X")
    if option == "A":
        loading(30, "Carregando menu do BITCOIN")
        funcionalidades.extras.investimentos.criptomoedas.bitcoin.main_bitcoin.bitcoin(USER=USER)
    elif option == "X":
        loading(20, "Voltando...")
        funcionalidades.extras.investimentos.main_investimentos.menu_investimentos_options(USER=USER)