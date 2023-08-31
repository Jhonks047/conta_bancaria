###################################################################################################

#TODO                           imports da pasta do programa

#?  CONFIG_PROGRAM
from config_program.config import *
from config_program.main_text import *

#?  FUNCIONALIDADES
import funcionalidades.extras.loterias.mixy_lottery.main_mixy
import funcionalidades.extras.main_extras

###################################################################################################

init(autoreset=True)


def menu_lottery_options():
    """Menu principal de loterias
    > Apenas mostra as opções disponíveis das loterias.
    """
    titulos("MENU DAS LOTERIAS")
    print()
    print(color_bright("   ( A ) MIXy.","l_m"))
    print()
    print(color_bright("( X ) Voltar.","l_r"))
    print()
    option = options_lottery()
    if option in "A":
        funcionalidades.extras.loterias.mixy_lottery.main_mixy.mixy_lottery()
    elif option in "X":
        loading(20, "Voltando...")
        funcionalidades.extras.main_extras.main_extras_menu()