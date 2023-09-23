###################################################################################################

#TODO                           imports da pasta do programa

import main
import tools.extras.investimentos.main_investimentos
import tools.extras.loterias.main_lottery
from config.get_informations import *
from config.main_text import *

###################################################################################################


def main_extras_menu(USER):
    """Menu principal de extras
    > Apenas mostra as opções disponíveis dos extras.
    """
    titulos("MENU DE EXTRAS")
    print(f"""
        {color("[ A ] Loterias.", "lgreen")}
        {color("[ B ] Investimentos", "lyellow")}
        
    {color("[ X ] Voltar.", "lred")}
        """)
    option = choices("A", "B", "X")
    if option == "A":
        loading(30, "Carregando menu de loterias")
        tools.extras.loterias.main_lottery.menu_lottery_options(USER=USER)
    elif option == "B":
        loading(30, "Carregando menu dos investimentos")
        tools.extras.investimentos.main_investimentos.menu_investimentos_options(USER=USER)
    elif option == "X":
        loading(20, "Voltando...")
        main.menu_principal(USER=USER)