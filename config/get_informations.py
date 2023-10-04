###################################################################################################

from firebase_admin import db

from config.main_text import *

###################################################################################################


#!  NÃO USAR
def loading(total: int, msg: str="loading"):
    """Barra de carregamento

    Args:
        total (INT): Definir o tamanho do tempo de carregamento
        msg (STR, optional): Mensagem para ser exibida ao lado da barra de carregamento. Padrão "loading".
    """
    from time import sleep

    from tqdm import tqdm
    print()
    for _ in tqdm(range(total), desc=Fore.LIGHTWHITE_EX+Style.BRIGHT+f"{msg}", ascii=False, ncols=50, bar_format="{l_bar}{bar}"+Style.RESET_ALL):
        sleep(0.05)
    print()


#!  Função para escolher opções do menu principal
def choices(*options):
    """Validar as escolhas do usuário
    
    Args:
        options: Recebe vários argumentos e armazena em uma tupla, para verificar se a opção escolhida pelo
            usuário bate com as opções usadas nesse argumento.
    
    Raises:
        ValueError: Causar uma exceção quando digitado um valor não permitido.

    Returns:
        STR: Retornar a < option > para o menu na qual ele foi chamado.
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
def options_SN():
    """Validar opções de SIM ou NÃO
    
        > [ S ] Confirmar transação.
        > [ N ] Cancelar transação.
    
    Raises:
        ValueError: Causar uma exceção quando digitado um valor não permitido

    Returns:
        STR: Retornar a < option > para o menu na qual ele foi chamado.
    """
    while True:
        try:
            print(f"""
    {color('[ S ] Confirmar transação', 'lgreen')}
    {color('[ N ] Cancelar transação', 'lred')}
                """)
            option = str(input(color("[ Digite a letra correspondente à ação desejada ]: ", "lwhite"))).strip().upper()
            if option not in ["S", "N"]:
                raise ValueError("Valor inválido!")
            else:
                break
        except ValueError as error:
            print(color(f"Erro: {error}","r"))
    return option


#!  Função para formatar o número em string com base na localidade
def formated_money(value: float):
    """Formatar um número para um valor monetário com base na região escolhida

    Args:
        value (FLOAT): Pega o valor e converte em string com a formatação adequada.

    Returns:
        STRING: Retorna o valor monetário com base na localidade.
    """
    import locale
    locale.setlocale(locale.LC_ALL, 'pt-BR')
    value = locale.format_string("%.2f", value, grouping=True)
    formated = f"{Fore.LIGHTGREEN_EX+Style.BRIGHT}{'R$ '}{Fore.LIGHTWHITE_EX}{value}"
    return formated


def pegar_informacoes_database(USER: str, sit: str):
    """PEGAR INFORMAÇÕES DENTRO DO BANCO DE DADOS

    Args:
        USER ( STR ): Usuário atual logado no sistema
        sit (str): 
                    >> "conta_bancaria": Pegar a informação da conta bancária do usuário.
                    >> "nome": Pegar o nome do usuário.
                    >> "bitcoins": Pegar a informação de bitcoins do usuário

    Returns:
        "nome": Retorna o nome do usuário com a cor magenta.
        "bitcoins": Retorna a quantia em bitcoins do usuário.
    """
    if sit == "conta_bancaria":
        try:
            users_ref = db.reference(f'users/{USER}/dados/dados_bancarios')
            conta_bancaria = users_ref.child('numero_da_conta').get()
        except Exception as error:
            print(f"Erro ao pegar o número da conta: {error}")
        else:
            return conta_bancaria
    elif sit == "nome":
        try:
            users_ref = db.reference(f'users/{USER}/dados/dados_bancarios')
            name = users_ref.child('display_name').get()
        except Exception as error:
            print(f"Erro ao pegar o nome da conta: {error}")
        else:
            return name
    elif sit == "bitcoins":
        try:
            users_ref = db.reference(f'users/{USER}/dados/dados_investimento/criptomoedas')
            bitcoins = users_ref.child('bitcoin').get()
        except Exception as error:
            print(f"Erro ao pegar o saldo de bitcoin: {error}")
        else:
            return bitcoins