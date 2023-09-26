import tools.extras.investimentos.criptomoedas.main_criptomoedas
import tools.extras.main_extras
from config.get_informations import *
from config.main_text import *


def menu_investimentos_options(USER):
    titulos("MENU DOS INVESTIMENTOS")
    print(f"""
        {color("[ A ] Criptomoedas", "lcyan")}
        
    {color("[ X ] Voltar", "lred")}
        """)
    option = choices("A", "X")
    if option == "A":
        tools.extras.investimentos.criptomoedas.main_criptomoedas.main_criptomoedas(USER=USER)
    elif option == "X":
        tools.extras.main_extras.main_extras_menu(USER=USER)
    