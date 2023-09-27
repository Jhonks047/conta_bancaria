###################################################################################################

from random import randint
from time import sleep

import main
import tools.extras.loterias.main_lottery
from config.get_informations import *
from config.main_balance import *
from config.main_text import *

###################################################################################################

#TODO                           imports da pasta do programa




###################################################################################################


def mixy_lottery(USER: str):
    """MENU DA LOTERIA MIXy
        Essa função mostra todo o menu da loteria MIXy, incluindo preço de cada bilhete e faixas de premiações.
        Dentro desse menu já existe um menu de opções com as seguintes opções:
            >   [ A ] Comprar bilhetes
            >   [ X ] Voltar
        Ao chamar a opção [ A ] o usuário define qual será a quantidade de bilhetes que deseja comprar, aparecendo
        o valor para ele confirmar a transação ou cancelar caso tenha informado errado a quantia que deseja comprar.
        Após definir a quantidade de bilhetes, o sistema irá verificar se possui saldo suficiente, e caso possua, irá
        chamar outra função chamada < mixy_tickets > para a criação dos bilhetes do usuário e o da máquina.
        
    Args:
        USER ( STR ): Usuário atual logado no sistema
    """

    titulos("LOTERIA MIXy")
    loading(15, "Carregando descrição")
    print()
    print(color(" COMO FUNCIONA: ","lred"))
    print(f"""
    {color("Você compra bilhetes que são numerados de 1 a 36, contendo 9 números cada.", "lcyan")}
    A máquina sorteia 1 único bilhete contendo apenas 6 números dentre os 36.
    O sorteio corre de forma automática após a compra dos bilhetes.
    As faixas de premiações são as seguintes:
    """)
    print(f"""                       {color('PREMIAÇÕES', 'lgreen')}
                {color('4 Acertos >> ', 'lblue')}{formated_money(value=6561)}
                {color('5 Acertos >> ', 'lcyan')}{formated_money(value=59049)}
                {color('6 Acertos >> ', 'lmagenta')}{formated_money(value=4782969)}
                """)
    print()
    print(f"{color('Preço por bilhete: ', 'lwhite')}{formated_money(value=9)}")
    main.actual_balance_str(USER=USER)
    print()
    print(color("     MENU DE OPÇÕES", "lred"))
    print(f"""
        {color('[ A ] Comprar bilhetes', 'lmagenta')}
        
    {color('[ X ] Voltar', 'lred')}
    """)
    confirm_menu = choices("A", "X")
    
    if confirm_menu == "A":
        ticket_price = 9 #!    Preço do ticket
        while True:
            titulos(msg="COMPRA DE TICKETS", cor="lgreen")
            try:
                while True:
                    tickets_usuario = int(input(color("[ Digite quantos bilhetes deseja comprar ]: ", "lwhite")))
                    if tickets_usuario <= 0:
                        raise ValueError("A quantidade de bilhetes não pode ser menor ou igual a 0!")
                    value_ticket = tickets_usuario * 9
                    loading(15, "Adicionando ao carrinho")
                    print(f"Sua compra ficou no valor de {formated_money(value=value_ticket)}")
                    confirm = options_SN()
                    if confirm == "S":
                        preco_total_tickets = ticket_price * tickets_usuario #!   Total do preço dos tickets
                        #!  Erro caso o valor dos tickets seja maior que o saldo disponível
                        if preco_total_tickets > atualizar_balance(USER=USER, sit="num"):
                            loading(30, "Voltando ao menu.")
                            main.menu_principal(USER=USER)
                        else:
                            atualizar_balance(USER=USER, amount=preco_total_tickets, sit="rem")
                            loading(30, "Processando pagamento")
                            print(color("Pagamento efetuado com sucesso!","lgreen"))
                            sleep(1)
                            print()
                            print(f"{'Você comprou '}{tickets_usuario}{' bilhetes, custando cerca de '}{formated_money(preco_total_tickets)}")
                            loading(20, "Gerando bilhetes, aguarde")
                            mixy_tickets(USER=USER, tickets=tickets_usuario)
                        break
                    else:
                        print("Voltando ao menu de compra de bilhetes.")
                        loading(20, "Voltando")
            except Exception as error:
                print(color(f"{'Erro: '}{error}","lred"))
                print()
    elif confirm_menu == "X":
        loading(20, "Voltando...")
        tools.extras.loterias.main_lottery.menu_lottery_options(USER=USER)

#!  Função para a criação dos tickets do sistema e do usuário
def mixy_tickets(USER: str, tickets: int):  
    """CRIAÇÃO DE TICKETS DO USUÁRIO E DO SISTEMA
        Essa função cria os tickets do usuário de acordo com a quantidade escolhida.

    Args:
        USER ( STR ): Usuário atual logado no sistema
        tickets ( INT ): Quantidade de bilhetes que o usuário comprou.
    """
    bilhete_sistema = []
    bilhetes_usuario = []
    total_bilhetes_usuario = []

    #?  Gerar um ticket da máquina com 6 números de 1 a 36
    while len(bilhete_sistema) <6:#!.....................................Tickets da máquina 
        mixy_ticket = randint(1, 36)
        if mixy_ticket not in bilhete_sistema:
            bilhete_sistema.append(mixy_ticket)
            bilhete_sistema.sort()

    #?  Gerar tickets do usuário com 9 números de 1 a 36
    while len(total_bilhetes_usuario) < tickets:#!.....................Tickets do usuário
        bilhetes_usuario.clear()
        while len(bilhetes_usuario) <9:
            mixy_ticket_user = randint(1, 36)
            if mixy_ticket_user not in bilhetes_usuario:
                bilhetes_usuario.append(mixy_ticket_user)
                bilhetes_usuario.sort()
        total_bilhetes_usuario.append(bilhetes_usuario[:])
    mixy_games(USER=USER, user_tickets=total_bilhetes_usuario, system_ticket=bilhete_sistema)


#!  Função para mostrar os jogos adquiridos pelo usuário
def mixy_games(USER: str, user_tickets: list, system_ticket: list):
    """LISTA OS BILHETES DO USUÁRIO E CONFERE COM O BILHETE DO SISTEMA

    Args:
        USER ( STR ): Todos os tickets gerados pelo usuário armazenado em uma lista.
        user_tickets ( LIST ): Bilhetes comprados pelo usuário.
        system_ticket ( LIST ): Bilhete gerado pelo sistema.
    """
    total_prize_amount = 0
    
    #  Mostrar os jogos feitos em linhas e numerados.
    for index, mixy in enumerate(user_tickets):
        print(color(f"{'Jogo'}{index+1}°:","lmagenta"),end=" ")
        print(color(mixy,"lyellow"))
        sleep(0.2)

    print()
    print(color(" O sistema irá sortear o bilhete. ","lmagenta"))
    loading(30, "Sorteando números")
    print()
    print(color("Bilhete gerado pela máquina:","lwhite"),end=" ")
    print(color(" | ".join(map(str, system_ticket)), "lyellow"))
    sleep(0.5)
    titulos("CONFERINDO BILHETES")
    loading(30, "Analisando acertos")

    #  Mostra o número de acertos de cada bilhete comparado ao sorteado do sistema
    for ind, value in enumerate(user_tickets):
        loading(10, f"Bilhete nº{ind+1}")
        print(f"", end=" > ")
        jogos = [num for num in value if num in system_ticket]
        if jogos:
            print(color(" | ".join(map(str, jogos)),"lgreen"))
            contador_numeros_acertos = len(jogos)
            if contador_numeros_acertos == 4:
                prize_amount = premiacoes_mixy(USER=USER, qnt_num=4)
                total_prize_amount += prize_amount
            if contador_numeros_acertos == 5:
                prize_amount = premiacoes_mixy(USER=USER, qnt_num=5)
                total_prize_amount += prize_amount
            if contador_numeros_acertos == 6:
                prize_amount = premiacoes_mixy(USER=USER, qnt_num=6)
                total_prize_amount += prize_amount
        else:
            print(color("Nenhum acerto!","red"))
    
    #   Mostra uma mensagem caso não tenha ganho nada na loteria
    if total_prize_amount <= 0:
        titulos(msg="NENHUM GANHO", cor="lred")
        print(f"""
    {color("Infelizmente você não ganhou nenhuma premiação!", "lcyan")}
    Deseja continuar as apostas?""")

    #  Mostra o valor total que foi ganho com os jogos comprados
    else:
        titulos(msg="GANHOS DA LOTERIA MIXy", cor="lgreen")
        print(f"{'Você ganhou no total: '}{formated_money(total_prize_amount)}")
        loading(60, f"Adicionando {formated_money(total_prize_amount)} ao saldo")
        main.actual_balance_str(USER=USER)
        print(color("Deseja continuar as apostas?", "lcyan"))
    confirm = options_SN()
    if confirm == "S":
        mixy_lottery(USER=USER)
    else:
        loading(10, "Voltando ao menu")
        main.menu_principal(USER=USER)


#  Função para premiar o usuário em caso de acertos
def premiacoes_mixy(USER: str, qnt_num: int):
    """PREMIAÇÕES MIXy
        Essa função define as faixas de premiações da loteria MIXy em caso de acertos.

    Args:
        USER ( STR ): Usuário atual logado no sistema
        qnt_num ( INT ): Argumento usado para verificar quantos acertos o usuário teve em um único bilhete para pagamento de prêmios.
    
    Return:
        A função retorna os valores de acordo com as premiações
    """
    # Faixas de premiações e seus valores
    premiacao_4_acertos = 6561
    premiacao_5_acertos = 59049
    premiacao_total = 4782969
    
    #  Acertos com 4 números.
    if qnt_num == 4:
        atualizar_balance(USER=USER, amount=premiacao_4_acertos, sit="add")
        print(color("Parabéns! Você acertou 4 números e foi premiado em","lgreen"),end=" ")
        print(formated_money(premiacao_4_acertos))
        return premiacao_4_acertos
    
    # Acertos com 5 números.
    if qnt_num == 5:
        atualizar_balance(USER=USER, amount=premiacao_5_acertos, sit="add")
        print(color("Parabéns! Você acertou 5 números e foi premiado em","green"),end=" ")
        print(formated_money(premiacao_5_acertos))
        return premiacao_5_acertos
    
    # Acertos com 6 números
    if qnt_num == 6:
        atualizar_balance(USER=USER, amount=premiacao_total, sit="add")
        print(color("Parabéns! Você acertou todos números e foi premiado em","green"),end=" ")
        print(formated_money(premiacao_total))
        return premiacao_total