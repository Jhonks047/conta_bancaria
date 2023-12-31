import tools.extras.investimentos.criptomoedas.bitcoin.main_bitcoin
import tools.extras.investimentos.main_investimentos
from config.get_informations import *
from config.main_text import *


def main_criptomoedas(USER):
    titulos("MENU DAS CRIPTOMOEDAS")
    print(f"""
        {color("[ A ] Bitcoin", "lyellow")}
        
    {color("[ X ] Voltar", "lred")}
    """)
    option = choices("A", "X")
    if option == "A":
        tools.extras.investimentos.criptomoedas.bitcoin.main_bitcoin.bitcoin(USER=USER)
    elif option == "X":
        tools.extras.investimentos.main_investimentos.menu_investimentos_options(USER=USER)