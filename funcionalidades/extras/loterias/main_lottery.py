###################################################################################################

#TODO                           imports da pasta do programa

#?  CONFIG_PROGRAM
from config_program.config import *
from config_program.main_text import *

#?  FUNCIONALIDADES
import funcionalidades.extras.loterias.mixy_lottery.main_mixy
import funcionalidades.extras.main_extras

###################################################################################################


def menu_lottery_options():
    """Menu principal de loterias
    > Apenas mostra as opções disponíveis das loterias.
    """
    titulos("MENU DAS LOTERIAS")
    print()
    print(color("   ( A ) MIXy.","lmagenta"))
    print()
    print(color("( X ) Voltar.","lred"))
    print()
    option = choices("A", "X")
    if option == "A":
        funcionalidades.extras.loterias.mixy_lottery.main_mixy.mixy_lottery()
    elif option == "X":
        loading(20, "Voltando...")
        funcionalidades.extras.main_extras.main_extras_menu()