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


def main_extras_menu():
    """Menu principal de extras
    > Apenas mostra as opções disponíveis dos extras.
    """
    print()
    titulos("MENU DE EXTRAS")
    print()
    print(color("   ( A ) Loterias.","lgreen"))
    print(color("   ( B ) Investimentos  ","lyellow"))
    print()
    print(color("( X ) Voltar.","lred"))
    print()
    option = choices("A", "B", "X")
    if option == "A":
        loading(30, "Carregando menu de loterias")
        funcionalidades.extras.loterias.main_lottery.menu_lottery_options()
    elif option == "B":
        loading(30, "Carregando menu dos investimentos")
        funcionalidades.extras.investimentos.main_investimentos.menu_investimentos_options()
    elif option == "X":
        loading(20, "Voltando...")
        main.MainBankAccount().menu_principal()