###################################################################################################

#TODO                           imports da pasta do programa

#?  MAIN
import main

#?  CONFIG_PROGRAM
from config_program.config import *
from config_program.main_text import *

#?  FUNCIONALIDADES
import funcionalidades.extras.loterias.main_lottery
import funcionalidades.extras.investimentos.main_investimentos

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
        funcionalidades.extras.loterias.main_lottery.menu_lottery_options(USER=USER)
    elif option == "B":
        loading(30, "Carregando menu dos investimentos")
        funcionalidades.extras.investimentos.main_investimentos.menu_investimentos_options(USER=USER)
    elif option == "X":
        loading(20, "Voltando...")
        main.menu_principal()