###################################################################################################

from random import randint
from time import sleep

###################################################################################################

#TODO                           imports da pasta do programa

#?  MAIN
import main

#?  CONFIG_PROGRAM
from config_program.config import *
from config_program.main_text import *
from config_program.main_balance import *

#?  FUNCIONALIDADES
import funcionalidades.extras.loterias.main_lottery

###################################################################################################


def mixy_lottery():
    """Menu da compra de tickets.

    Raises:
        ValueError: Retornar um erro caso o usuário digite um valor inválido ou a quantidade de bilhetes == 0
    """
    titulos(f"LOTERIA MIXy")
    loading(15, "Carregando descrição")
    print(main.MainBankAccount().actual_balance_str())
    print()
    print(color_bright(" COMO FUNCIONA: ","r_b"))
    sleep(0.3)
    print(color_bright("    Você compra bilhetes que são numerados de 1 a 36, contendo 9 números cada.","g"))
    print(color_bright("    A máquina sorteia 1 único bilhete contendo apenas 6 números dentre os 36.","g"))
    print(color_bright("    As faixas de premiações são as seguintes:","g"))
    print()
    print(color_bright(" PREMIAÇÕES ","m_b"))
    sleep(0.3)
    print(f"    {'4 Acertos >> '}{formated_money(6561)}")
    sleep(0.3)
    print(f"    {'5 Acertos >> '}{formated_money(59049)}")
    sleep(0.3)
    print(f"    {'6 Acertos >> '}{formated_money(4782969)}")
    sleep(0.3)
    print()
    print(color_bright(" Preço por bilhete:","l_w"), end=" ")
    print(formated_money(9))
    titulos("OPÇÕES DISPONÍVEIS")
    print(color_bright("   ( A ) Comprar bilhetes.","g"))
    print()
    print(color_bright("( X ) Voltar","l_r"))
    print()
    confirm_menu = options_lottery()
    if confirm_menu in "A":
        while True:
            titulos("COMPRA DE TICKETS")
            try:
                while True:
                    qnt_tickets = int(input("Digite quantos bilhetes deseja comprar: "))
                    if qnt_tickets <= 0:
                        raise ValueError("A quantidade de bilhetes não pode ser menor ou igual a 0!")
                    value_ticket = qnt_tickets * 9
                    loading(15, "Adicionando ao carrinho")
                    print(f"Sua compra ficou no valor de {formated_money(value_ticket)}")
                    confirm = continue_options()
                    if confirm == "S":
                        mixy_tickets(qnt_tickets)
                        break
                    else:
                        print("Voltando ao menu de compra de bilhetes.")
                        loading(20, "Voltando")
            except Exception as error:
                print(color_bright(f"{'Erro: '}{error}","l_r"))
                print()
    elif confirm_menu in "X":
        loading(20, "Voltando...")
        funcionalidades.extras.loterias.main_lottery.menu_lottery_options()


#!  Função para a criação dos tickets do sistema e do usuário
def mixy_tickets(qnt_tickets):
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
    while len(total_tickets_users) < qnt_tickets:#!.....................Tickets do usuário
        tickets_users.clear()
        while len(tickets_users) <9:
            mixy_ticket_user = randint(1, 36)
            if mixy_ticket_user not in tickets_users:
                tickets_users.append(mixy_ticket_user)
                tickets_users.sort()
        total_tickets_users.append(tickets_users[:])
    mixy_games(total_tickets_users, ticket_system, qnt_tickets)


#!  Função para mostrar os jogos adquiridos pelo usuário
def mixy_games(user_tickets, system_ticket, total_buyed_tickets):
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
    if total_price_ticket > update_balance():
        print(insufficient_balance())
        print(text_menu_principal())
        loading(30, "Voltando ao menu.")
        main.MainBankAccount.menu_principal()
    else:
        update_balance(total_price_ticket, "rem")
        loading(30, "Processando pagamento")
        print(color_bright("Pagamento efetuado com sucesso!","l_g"))
        sleep(1)
        print()
        print(f"{'Você comprou '}{qnt_tickets}{' bilhetes, custando cerca de '}{formated_money(total_price_ticket)}")
        loading(20, "Gerando bilhetes, aguarde")
        
        #!  Mostrar os jogos feitos em linhas e numerados.
        for index, mixy in enumerate(total_tickets_users):
            print(color_bright(f"{'Jogo'}{index+1}°:","l_m"),end=" ")
            print(color_bright(mixy,"l_y"))
            sleep(0.2)
        
        print()
        print(color_bright(" O sistema irá sortear o bilhete. ","r_b"))
        loading(30, "Sorteando números")
        print()
        print(color_bright("Bilhete gerado pela máquina:","l_w"),end=" ")
        print(color_bright(" | ".join(map(str, ticket_system)), "l_y"))
        sleep(0.5)
        titulos("CONFERINDO BILHETES")
        loading(30, "Analisando acertos")
        
        #!  Mostrar o número de acertos de cada bilhete comparado ao sorteado
        for ind, value in enumerate(total_tickets_users):
            loading(10, f"Bilhete nº{ind+1}")
            print(f"", end=" > ")
            jogos = [num for num in value if num in ticket_system]
            if jogos:
                print(color_bright(" | ".join(map(str, jogos)),"l_g"))
                contador_numeros_acertos = len(jogos)
                if contador_numeros_acertos == 4:
                    prize_amount = premiacoes_mixy(4)
                    total_prize_amount += prize_amount
                if contador_numeros_acertos == 5:
                    prize_amount = premiacoes_mixy(5)
                    total_prize_amount += prize_amount
                if contador_numeros_acertos == 6:
                    prize_amount = premiacoes_mixy(6)
                    total_prize_amount += prize_amount
            else:
                print(color_bright("Nenhum acerto!","r"))
    
    #!  Mostrar o valor total que foi ganho com os jogos comprados
    if prize_amount <= 0:
        titulos("NENHUM GANHO")
    else:
        titulos("GANHOS DA LOTERIA MIXy")
        print(f"{'Você ganhou no total: '}{formated_money(total_prize_amount)}")
        loading(60, f"Adicionando {formated_money(total_prize_amount)} ao saldo")
        print(main.MainBankAccount.actual_balance_str())
    confirm = continue_options()
    if confirm == "S":
        mixy_lottery()
    else:
        text_menu_principal()
        loading(10, "Voltando ao menu")
        main.MainBankAccount.menu_principal()


#!  Função para premiar o usuário em caso de acertos
def premiacoes_mixy(qnt_num=0):
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
        update_balance(main.MainBankAccount.name, premiacao_4_acertos, "add")
        print(color_bright("Parabéns! Você acertou 4 números e foi premiado em","l_g"),end=" ")
        print(formated_money(premiacao_4_acertos))
        return premiacao_4_acertos
    
    #! Acertos com 5 números.
    if qnt_num == 5:
        update_balance(main.MainBankAccount.name, premiacao_5_acertos, "add")
        print(color_bright("Parabéns! Você acertou 5 números e foi premiado em","g"),end=" ")
        print(formated_money(premiacao_5_acertos))
        return premiacao_5_acertos
    
    #! Acertos com 6 números
    if qnt_num == 6:
        update_balance(main.MainBankAccount.name, premiacao_total, "add")
        print(color_bright("Parabéns! Você acertou todos números e foi premiado em","g"),end=" ")
        print(formated_money(premiacao_total))
        return premiacao_total