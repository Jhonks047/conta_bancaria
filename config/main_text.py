###################################################################################################

from colorama import Fore, Style, init

###################################################################################################

init(autoreset=True)

def titulos(msg, cor="magenta"):
    """Mostrar um texto em formato de TÍTULO, com =- em cima e em baixo, com o texto centralizado

    Args:
        msg (STR): Pegar o valor digitado pelo usuário e converter em formato de TÍTULO
    """
    width = 60
    print()
    print("=-" * 30)
    print(color(f"{msg.center(width)}",cor))
    print("=-" * 30)


def text_menu_principal():
    return f"{color('Voltando ao menu principal!', 'lyellow')}"


def insufficient_balance():
    return f"{color('Saldo insuficiente!', 'lred')}"


#!  Função para definir uma cor com BRIGHT
def color(text, sit):
    """Alterar a cor da frase/texto

    Args:
        text (STRING): Aqui será definido o texto/mensagem que o usuário irá colocar cores.
        sit (STRING): Definir a cor que será usada.
            Cores disponíveis:
            
                - red  |  lred
                - green  |  lgreen
                - blue  |  lblue
                - magenta  |  lmagenta
                - cyan  |  lcyan
                - yellow  |  lyellow
                - white  |  lwhite
                
            As cores que possuem o " l " antes do tipo da cor é para indicar que a cor é mais clara
    """
    sit = str(sit).lower()
#TODO......................NORMAL COLORS......................

    if sit == "red":
        return f"{Fore.RED+Style.BRIGHT}{text}"
    elif sit == "green":
        return f"{Fore.GREEN+Style.BRIGHT}{text}"
    elif sit == "blue":
        return f"{Fore.BLUE+Style.BRIGHT}{text}"
    elif sit == "magenta":
        return f"{Fore.MAGENTA+Style.BRIGHT}{text}"
    elif sit == "cyan":
        return f"{Fore.CYAN+Style.BRIGHT}{text}"
    elif sit == "yellow":
        return f"{Fore.YELLOW+Style.BRIGHT}{text}"
    elif sit == "white":
        return f"{Fore.WHITE+Style.BRIGHT}{text}"
    
#TODO......................LIGHT COLORS......................

    elif sit == "lred":
        return f"{Fore.LIGHTRED_EX+Style.BRIGHT}{text}"
    elif sit == "lgreen":
        return f"{Fore.LIGHTGREEN_EX+Style.BRIGHT}{text}"
    elif sit == "lblue":
        return f"{Fore.LIGHTBLUE_EX+Style.BRIGHT}{text}"
    elif sit == "lmagenta":
        return f"{Fore.LIGHTMAGENTA_EX+Style.BRIGHT}{text}"
    elif sit == "lcyan":
        return f"{Fore.LIGHTCYAN_EX+Style.BRIGHT}{text}"
    elif sit == "lyellow":
        return f"{Fore.LIGHTYELLOW_EX+Style.BRIGHT}{text}"
    elif sit == "lwhite":
        return f"{Fore.LIGHTWHITE_EX+Style.BRIGHT}{text}"