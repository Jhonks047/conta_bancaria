from config_program.config import *
from config_program.main_text import *
import funcionalidades.extras.main_extras



def menu_investimentos_options():
    titulos("MENU DOS INVESTIMENTOS")
    print()
    print(f"""
        {color("[ A ] Criptomoedas", "lcyan")}
        
    {color("[ X ] Voltar", "lred")}
        """)
    print()
    option = choices("A", "X")
    