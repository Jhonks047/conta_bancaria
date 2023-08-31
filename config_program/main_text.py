###################################################################################################

from colorama import Fore, Style, init

###################################################################################################

from config_program.config import color_bright

init(autoreset=True)


def titulos(msg):
    """Mostrar um texto em formato de TÍTULO, com =- em cima e em baixo, com o texto centralizado

    Args:
        msg (STR): Pegar o valor digitado pelo usuário e converter em formato de TÍTULO
    """
    width = 60
    print()
    print("=-" * 30)
    print(color_bright(f"{msg.center(width)}","m"))
    print("=-" * 30)


def text_menu_principal():
    return f"{Fore.LIGHTYELLOW_EX + Style.BRIGHT}{'Voltando ao menu principal!'}"


def insufficient_balance():
    return f"{Fore.RED + Style.BRIGHT}{'Saldo insuficiente!'}"