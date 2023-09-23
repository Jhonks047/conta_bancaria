###################################################################################################

from config_program.config import color

###################################################################################################


def titulos(msg):
    """Mostrar um texto em formato de TÍTULO, com =- em cima e em baixo, com o texto centralizado

    Args:
        msg (STR): Pegar o valor digitado pelo usuário e converter em formato de TÍTULO
    """
    width = 60
    print()
    print("=-" * 30)
    print(color(f"{msg.center(width)}","magenta"))
    print("=-" * 30)


def text_menu_principal():
    return f"{color('Voltando ao menu principal!', 'lyellow')}"


def insufficient_balance():
    return f"{color('Saldo insuficiente!', 'lred')}"