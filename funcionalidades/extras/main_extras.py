###################################################################################################

#TODO                           imports da pasta do programa

#?  MAIN
import main

#?  CONFIG_PROGRAM
from config_program.config import *
from config_program.main_text import *

#?  FUNCIONALIDADES
import funcionalidades.extras.loterias.main_lottery

###################################################################################################


def main_extras_menu():
    """Menu principal de extras
    > Apenas mostra as opções disponíveis dos extras.
    """
    print()
    titulos("MENU DE EXTRAS")
    print()
    print(color_bright("   ( A ) Loterias.","l_g"))
    print(color_bright("   ( B ) Investimentos  ","l_y"))
    print()
    print(color_bright("( X ) Voltar.","l_r"))
    print()
    option = options_extras()
    if option in "A":
        loading(30, "Carregando menu de loterias")
        funcionalidades.extras.loterias.main_lottery.menu_lottery_options()
    elif option in "X":
        loading(20, "Voltando...")
        main.MainBankAccount().menu_principal()