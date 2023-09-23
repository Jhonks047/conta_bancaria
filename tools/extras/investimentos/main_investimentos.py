import tools.extras.investimentos.criptomoedas.main_criptomoedas
import tools.extras.main_extras
from config.get_informations import *
from config.main_text import *


def menu_investimentos_options(USER):
    titulos("MENU DOS INVESTIMENTOS")
    print()
    print(f"""
        {color("[ A ] Criptomoedas", "lcyan")}
        
    {color("[ X ] Voltar", "lred")}
        """)
    print()
    option = choices("A", "X")
    if option == "A":
        loading(30, "Carregando menu das criptomoedas")
        tools.extras.investimentos.criptomoedas.main_criptomoedas.main_criptomoedas(USER=USER)
    elif option == "X":
        loading(20, "Voltando...")
        tools.extras.main_extras.main_extras_menu(USER=USER)
    