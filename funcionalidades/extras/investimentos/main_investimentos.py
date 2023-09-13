from config_program.config import *
from config_program.main_text import *
import funcionalidades.extras.main_extras
import funcionalidades.extras.investimentos.criptomoedas.main_criptomoedas


def menu_investimentos_options():
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
        funcionalidades.extras.investimentos.criptomoedas.main_criptomoedas.main_criptomoedas()
    elif option == "X":
        loading(20, "Voltando...")
        funcionalidades.extras.main_extras.main_extras_menu()
    