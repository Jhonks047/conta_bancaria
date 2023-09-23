###################################################################################################

from colorama import Fore, Style, init
from firebase_admin import db

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
def choices(*options):
    """Validar as ações do player
    
    Raises:
        ValueError: Causar uma exceção quando digitado um valor não permitido

    Returns:
        STR: Retornar a option para o menu na qual ele foi chamado.
    """
    while True:
        try:
            option = str(input(color("[ Digite a letra correspondente à ação desejada ]: ", "lwhite"))).strip().upper()
            if option not in options:
                raise ValueError("Valor inválido!")
            else:
                break
        except ValueError as error:
            print(f"Erro: {error}")
    return option


#!  Função para continuar uma execução ou não
def options_SN(text):
    """Validar opções
    
    Raises:
        ValueError: Causar uma exceção quando digitado um valor não permitido

    Returns:
        STR: Retornar a option para o menu na qual ele foi chamado.
    """
    while True:
        try:
            option = input(f"{text}: ").strip().upper()
            if option not in ["S", "N"]:
                raise ValueError("Valor inválido!")
            else:
                break
        except ValueError as error:
            print(color(f"Erro: {error}","r"))
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


def pegar_informacoes_database(USER, sit=""):
    if sit == "conta_bancaria":
        try:
            users_ref = db.reference(f'users/{USER}/dados/dados_bancarios')
            conta_bancaria = users_ref.child('numero_da_conta').get()
        except Exception as error:
            print(f"Erro ao pegar o número da conta: {error}")
        else:
            print(f"{color('Número da conta: ', 'lcyan')}{color(conta_bancaria, 'lyellow')}")
    elif sit == "nome":
        try:
            users_ref = db.reference(f'users/{USER}/dados/dados_bancarios')
            name = users_ref.child('display_name').get()
        except Exception as error:
            print(f"Erro ao pegar o nome da conta: {error}")
        else:
            return f"{color(name, 'lmagenta')}"
    elif sit == "bitcoins":
        try:
            users_ref = db.reference(f'users/{USER}/dados/dados_investimento/criptomoedas')
            bitcoins = users_ref.child('bitcoin').get()
        except Exception as error:
            print(f"Erro ao pegar o saldo de bitcoin: {error}")
        else:
            return bitcoins