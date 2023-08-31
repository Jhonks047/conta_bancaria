###################################################################################################

from colorama import Fore, Style, Back, init

###################################################################################################

init(autoreset=True)

#!  Função que simula uma barra de carregamento
def loading(total, msg="loading"):
    """Barra de carregamento

    Args:
        total (INT): Definir o tamanho do tempo de carregamento
        msg (str, optional): Mensagem para ser exibida ao lado da barra de carregamento. Padrão "loading".
    """
    from time import sleep
    from tqdm import tqdm
    print()
    for _ in tqdm(range(total), desc=Fore.LIGHTWHITE_EX+Style.BRIGHT+f"{msg}", ascii=False, ncols=50, bar_format="{l_bar}{bar}"+Style.RESET_ALL):
        sleep(0.05)
    print()


#!  Função para escolher opções do menu principal
def options_menu():
    """Validar opções menu
    
    Raises:
        ValueError: Causar uma exceção quando digitado um valor não permitido

    Returns:
        STR: Retornar a option para o menu na qual ele foi chamado.
    """
    while True:
        try:
            option = str(input(f"Digite uma opção: ")).strip().upper()
            if option not in ["A", "B", "C", "X"]:
                raise ValueError("Valor inválido!")
            else:
                break
        except ValueError as error:
            print(color_bright(f"Erro: {error}","r"))
    return option


#!  Função para continuar uma execução ou não
def continue_options():
    """Apenas perguntar se o usuário quer continuar com uma execução ou não.

    Raises:
        ValueError: Causa uma exceção caso o usuário digite um valor fora do permitido.

    Returns:
        STRING: Retorna a escolha do usuário
    """
    while True:
        try:
            option = str(input(f"Deseja continuar? "
                                f"[ {Fore.LIGHTGREEN_EX+Style.BRIGHT}{'S '}{Style.RESET_ALL}"
                                f"/ {Fore.LIGHTRED_EX+Style.BRIGHT}{'N'}{Style.RESET_ALL} ]: ")).upper().strip()
            if option not in ["S", "N"]:
                raise ValueError("Valor inválido!")
            else:
                break
        except ValueError as error:
            print(color_bright(f"Erro: {error}","r"))
    return option


#!  Função para escolher opções do menu de extras
def options_extras():
    """Validar opções extras
    
    Raises:
        ValueError: Causar uma exceção quando digitado um valor não permitido

    Returns:
        STR: Retornar a option para o menu na qual ele foi chamado.
    """
    while True:
        try:
            option = str(input(f"Digite uma opção: ")).strip().upper()
            if option not in ["A", "B", "X"]:
                raise ValueError("Valor inválido!")
            else:
                break
        except ValueError as error:
            print(color_bright(f"Erro: {error}","r"))
    return option


#!  Função para escolher opções do menu de loterias
def options_lottery():
    """Validar opções loterias
    
    Raises:
        ValueError: Causar uma exceção quando digitado um valor não permitido

    Returns:
        STR: Retornar a option para o menu na qual ele foi chamado.
    """
    while True:
        try:
            option = str(input(f"Digite uma opção: ")).strip().upper()
            if option not in ["A", "X"]:
                raise ValueError("Valor inválido!")
            else:
                break
        except ValueError as error:
            print(color_bright(f"Erro: {error}","r"))
    return option


#!  Função para formatar o número em string com base na localidade
def formated_money(value):
    """Formatar um número para um valor monetário com base na região escolhida

    Args:
        value (FLOAT): Pega o valor value e converte em string com a formatação adequada.

    Returns:
        STRING: Retorna o valor monetário com base na localidade.
    """
    import locale
    locale.setlocale(locale.LC_ALL, 'pt-BR')
    value = locale.format_string("%.2f", value, grouping=True)
    formated = f"{Fore.LIGHTGREEN_EX+Style.BRIGHT}{'R$ '}{Fore.LIGHTWHITE_EX}{value}"
    return formated


#!  Função para definir uma cor com BRIGHT
def color_bright(msg, type=""):
#TODO           LIGHT COLORS
    if type in "l_g":
        return f"{Fore.LIGHTGREEN_EX+Style.BRIGHT}{msg}"
    elif type in "l_r":
        return f"{Fore.LIGHTRED_EX+Style.BRIGHT}{msg}"
    elif type in "l_w":
        return f"{Fore.LIGHTWHITE_EX+Style.BRIGHT}{msg}"
    elif type in "l_y":
        return f"{Fore.LIGHTYELLOW_EX+Style.BRIGHT}{msg}"
    elif type in "l_m":
        return f"{Fore.LIGHTMAGENTA_EX+Style.BRIGHT}{msg}"
#TODO           BACKGROUND COLORS
    elif type in "r_b":
        return f"{Back.RED+Fore.LIGHTWHITE_EX+Style.BRIGHT}{msg}"
    elif type in "m_b":
        return f"{Back.MAGENTA+Fore.LIGHTWHITE_EX+Style.BRIGHT}{msg}"
    elif type in "g_b":
        return f"{Back.GREEN+Fore.BLACK+Style.BRIGHT}{msg}"
#TODO           NORMAL COLORS
    elif type in "g":
        return f"{Fore.GREEN+Style.BRIGHT}{msg}"
    elif type in "r":
        return f"{Fore.RED+Style.BRIGHT}{msg}"