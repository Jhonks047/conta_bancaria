###################################################################################################

from random import randint
from time import sleep

###################################################################################################

#TODO                           imports da pasta do programa

#?  MAIN
import main

#?  CONFIG_PROGRAM
from config.get_informations import *
from config.main_text import *
from config.main_balance import *

#?  FUNCIONALIDADES
import tools.extras.loterias.main_lottery

###################################################################################################


def mixy_lottery(USER):
    """Menu da compra de tickets.

    Raises:
        ValueError: Retornar um erro caso o usuário digite um valor inválido ou a quantidade de bilhetes == 0
    """
    titulos("LOTERIA MIXy")
    loading(15, "Carregando descrição")
    print()
    print(color(" COMO FUNCIONA: ","lred"))
    print("""
        Você compra bilhetes que são numerados de 1 a 36, contendo 9 números cada.
        A máquina sorteia 1 único bilhete contendo apenas 6 números dentre os 36.
        O sorteio corre de forma automática após a compra dos bilhetes.
        As faixas de premiações são as seguintes:""")
    print()
    print(f"""                       {color('PREMIAÇÕES', 'lgreen')}
                {color('4 Acertos >> ', 'lblue')}{formated_money(value=6561)}
                {color('5 Acertos >> ', 'lcyan')}{formated_money(value=59049)}
                {color('6 Acertos >> ', 'lmagenta')}{formated_money(value=4782969)}
                """)
    print()
    print(f"{color('Preço por bilhete: ', 'lwhite')}{formated_money(value=9)}")
    titulos("OPÇÕES DISPONÍVEIS")
    main.actual_balance_str(USER=USER)
    print(f"""
        {color('[ A ] Comprar bilhetes', 'lmagenta')}
        
    {color('[ X ] Voltar', 'lred')}
    """)
    confirm_menu = choices("A", "X")
    if confirm_menu == "A":
        while True:
            titulos("COMPRA DE TICKETS")
            try:
                while True:
                    tickets_usuario = int(input("Digite quantos bilhetes deseja comprar: "))
                    if tickets_usuario <= 0:
                        raise ValueError("A quantidade de bilhetes não pode ser menor ou igual a 0!")
                    value_ticket = tickets_usuario * 9
                    loading(15, "Adicionando ao carrinho")
                    print(f"Sua compra ficou no valor de {formated_money(value=value_ticket)}")
                    confirm = options_SN()
                    if confirm == "S":
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
        tools.extras.loterias.main_lottery.menu_lottery_options()


#!  Função para a criação dos tickets do sistema e do usuário
def mixy_tickets(USER, tickets):
    """Criar tickets do usuário e do sistema para o sorteio da loteria

    Args:
        qnt_tickets (INT): Quantidade de bilhetes que o usuário comprou.
    """
    ticket_system = []
    tickets_users = []
    total_tickets_users = []

    #?  Gerar um ticket da máquina com 6 números de 1 a 36
    while len(ticket_system) <6:#!.....................................Tickets da máquina
        mixy_ticket = randint(1, 36)
        if mixy_ticket not in ticket_system:
            ticket_system.append(mixy_ticket)
            ticket_system.sort()

    #?  Gerar tickets do usuário com 9 números de 1 a 36
    while len(total_tickets_users) < tickets:#!.....................Tickets do usuário
        tickets_users.clear()
        while len(tickets_users) <9:
            mixy_ticket_user = randint(1, 36)
            if mixy_ticket_user not in tickets_users:
                tickets_users.append(mixy_ticket_user)
                tickets_users.sort()
        total_tickets_users.append(tickets_users[:])
    mixy_games(USER=USER, user_tickets=total_tickets_users, system_ticket=ticket_system, total_buyed_tickets=tickets)


#!  Função para mostrar os jogos adquiridos pelo usuário
def mixy_games(USER, user_tickets, system_ticket, total_buyed_tickets):
    """Lista os jogos adquiridos e define o valor dos tickets

    Args:
        list1 (LIST): Todos os tickets gerados pelo usuário armazenado em uma lista
        list2 (INT): Ticket gerado pelo sistema
        tickets (INT): Total de tickets comprados pelo usuário
    """
    total_tickets_users = user_tickets
    ticket_system = system_ticket
    qnt_tickets = total_buyed_tickets
    total_prize_amount = 0
    prize_amount = 0
    ticket_price = 9 #!    Preço do ticket
    total_price_ticket = ticket_price * qnt_tickets #!   Total do preço dos tickets
    
    #!  Erro caso o valor dos tickets seja maior que o saldo disponível
    if total_price_ticket > atualizar_balance(USER=USER, sit="num"):
        print(insufficient_balance())
        print(text_menu_principal())
        loading(30, "Voltando ao menu.")
        main.menu_principal(USER=USER)
    else:
        atualizar_balance(USER=USER, amount=total_price_ticket, sit="rem")
        loading(30, "Processando pagamento")
        print(color("Pagamento efetuado com sucesso!","lgreen"))
        sleep(1)
        print()
        print(f"{'Você comprou '}{qnt_tickets}{' bilhetes, custando cerca de '}{formated_money(total_price_ticket)}")
        loading(20, "Gerando bilhetes, aguarde")
        
        #!  Mostrar os jogos feitos em linhas e numerados.
        for index, mixy in enumerate(total_tickets_users):
            print(color(f"{'Jogo'}{index+1}°:","lmagenta"),end=" ")
            print(color(mixy,"lyellow"))
            sleep(0.2)
        
        print()
        print(color(" O sistema irá sortear o bilhete. ","lmagenta"))
        loading(30, "Sorteando números")
        print()
        print(color("Bilhete gerado pela máquina:","lwhite"),end=" ")
        print(color(" | ".join(map(str, ticket_system)), "lyellow"))
        sleep(0.5)
        titulos("CONFERINDO BILHETES")
        loading(30, "Analisando acertos")
        
        #!  Mostrar o número de acertos de cada bilhete comparado ao sorteado
        for ind, value in enumerate(total_tickets_users):
            loading(10, f"Bilhete nº{ind+1}")
            print(f"", end=" > ")
            jogos = [num for num in value if num in ticket_system]
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
    
    #!  Mostrar o valor total que foi ganho com os jogos comprados
    if prize_amount <= 0:
        titulos("NENHUM GANHO")
    else:
        titulos("GANHOS DA LOTERIA MIXy")
        print(f"{'Você ganhou no total: '}{formated_money(total_prize_amount)}")
        loading(60, f"Adicionando {formated_money(total_prize_amount)} ao saldo")
        main.actual_balance_str(USER=USER)
    confirm = options_SN()
    if confirm == "S":
        mixy_lottery(USER=USER)
    else:
        text_menu_principal()
        loading(10, "Voltando ao menu")
        main.menu_principal(USER=USER)


#!  Função para premiar o usuário em caso de acertos
def premiacoes_mixy(USER, qnt_num=0):
    """Define a premiação em caso de acertos

    Args:
        qnt_num (INT): Valor de números de acertos da função mixy_games() para definir a premiação
    """
    #! Faixas de premiações e seus valores
    premiacao_4_acertos = 6561
    premiacao_5_acertos = 59049
    premiacao_total = 4782969
    
    #!  Acertos com 4 números.
    if qnt_num == 4:
        atualizar_balance(USER=USER, amount=premiacao_4_acertos, sit="add")
        print(color("Parabéns! Você acertou 4 números e foi premiado em","lgreen"),end=" ")
        print(formated_money(premiacao_4_acertos))
        return premiacao_4_acertos
    
    #! Acertos com 5 números.
    if qnt_num == 5:
        atualizar_balance(USER=USER, amount=premiacao_5_acertos, sit="add")
        print(color("Parabéns! Você acertou 5 números e foi premiado em","green"),end=" ")
        print(formated_money(premiacao_5_acertos))
        return premiacao_5_acertos
    
    #! Acertos com 6 números
    if qnt_num == 6:
        atualizar_balance(USER=USER, amount=premiacao_total, sit="add")
        print(color("Parabéns! Você acertou todos números e foi premiado em","green"),end=" ")
        print(formated_money(premiacao_total))
        return premiacao_total