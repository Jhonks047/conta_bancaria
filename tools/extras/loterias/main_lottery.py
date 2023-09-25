###################################################################################################

#TODO                           imports da pasta do programa

import tools.extras.loterias.mixy_lottery.main_mixy
import tools.extras.main_extras
from config.get_informations import *
from config.main_text import *

###################################################################################################


def menu_lottery_options(USER):
    """Menu principal de loterias
    > Apenas mostra as opções disponíveis das loterias.
    """
    titulos("MENU DAS LOTERIAS")
    print(f"""
        {color("[ A ] Loteria MIXy", "lmagenta")}
        
    {color("[ X ] Voltar", "lred")}
    """)
    option = choices("A", "X")
    if option == "A":
        tools.extras.loterias.mixy_lottery.main_mixy.mixy_lottery(USER=USER)
    elif option == "X":
        tools.extras.main_extras.main_extras_menu()