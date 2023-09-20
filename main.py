###################################################################################################
#TODO                           Outros imports
from time import sleep

###################################################################################################

#TODO                           Imports da pasta do programa

#?  CONFIG_PROGRAM
from config_program.main_balance import *
from config_program.main_text import *
from config_program.config_informations_user import *
from config_program.config import *
from config_program.validar_login import *

#?  FUNCIONALIDADES
from funcionalidades.transacoes_bancarias.main_transactions import *
import funcionalidades.extras.main_extras

###################################################################################################

#TODO                              COISAS A FAZER
#TODO   | LEGENDA
#!  | Importante *
#?  | Otimização
#*  | 

#!  [x] Alterar o run() para salvar os dados em um banco de dados ao invés de criar arquivos.
#!  [ ] Salvar dados monetários, bilhetes e criptomoedas no banco de dados.
#!  [ ] 
#?  [ ] Criar uma interface de cadastro e login de usuário mais detalhada.
#?  [ ] Ajustar as telas de loading com outras informações e visivelmente mais agradável.

###################################################################################################


#!  Mostrar menu principal

def run():
    global USER
    titulos("ÁREA DO USUÁRIO")
    print("""
        Olá! Seja bem vindo ao banco MKL! Escolha uma opção abaixo do que deseja:
        
        [ A ] Fazer login
        [ B ] Cadastrar-se
        
    [ X ] Sair do programa
    """)
    choice = choices("A", "B", "X")
    if choice == "A":
        contador = 0
        while contador < 3:
            try:
                user = fazer_login()
                USER = user.uid
                print(USER)
                if user:
                    print("Login efetuado com sucesso!")
                    print(USER)
                    break
                else:
                    contador += 1
                    continue
            except:
                continue
        if contador == 3:
            print("Excedeu o limite, fechando programa por segurança!")
        menu_principal(USER)
    elif choice == "B":
        while True:
            try:
                titulos("CADASTRAMENTO DE USUÁRIO")
                name = str(input("Digite seu nome: ")).capitalize().strip()
                password = str(input("Digite uma senha para o cadastro: ")).strip()
                username = gerarUser(name)
                uid = gerar_uid(username)
                email = gerar_email(name)
                criar_usuario(email=email, senha=password, uid=uid)
                criar_informacoes(uid)
            except:
                continue
            else:
                contador = 0
                while contador < 3:
                    try:
                        user = fazer_login()
                        USER = user.uid
                        if user:
                            print("Login efetuado com sucesso!")
                            break
                        else:
                            contador += 1
                            continue
                    except:
                        continue
                if user:
                    break
                if contador == 3:
                    print("Excedeu o limite, fechando programa por segurança!")
        menu_principal(USER)
            
def menu_principal(USER):
    """Mostra o menu principal junto a função actual_balance_str()
    """
    titulos("SEJA BEM VINDO AO MENU PRINCIPAL DO BANCO NSX")
    #print(actual_balance_str())
    loading(30, "Carregando menu de opções")
    menu_options(USER)


#!  Mostrar saldo disponivel
#def actual_balance_str():
    """Formata o saldo atual em string para mostrar corretamente o valor monetário.

    Returns:
        STRING: Retorna a frase SALDO DISPONÍVEL junto ao saldo ja formatado para a região pt-BR
    """
    print()
    import locale
    locale.setlocale(locale.LC_ALL, 'pt-BR')
    balance_actual = ""
    balance_actual = round(balance_actual, 2)
    balance_actual_str = locale.format_string("%.2f", balance_actual, grouping=True)
    actual_balance = color("Saldo disponível: R$ ","lgreen")+color(balance_actual_str, "lwhite")
    return actual_balance


#!  Mostrar opções do menu principal
def menu_options(USER):
    """Menu de opções bancárias
    >   ( A )   Depositar
    >   ( B )   Sacar
    >   ( C )   Extras
    >   ( X )   Sair do programa
    
        Raises:
            Opção ( B ): Causar uma exceção caso o usuário tente sacar um valor acima do saldo.
    """
    titulos("MENU DE OPÇÕES")
    print()
    print(color("   ( A ) Deposit.","lgreen"))
    print(color("   ( B ) Withdraw.","lyellow"))
    print(color("   ( C ) Extras.","lmagenta"))
    print()
    print(color("( X ) Sair do programa.","lred"))
    print()
    option = choices("A", "B", "C", "X")
    
    #!  Chama a função do depósito.
    if option == "A":
        loading(30, "Carregando opção DEPÓSITO")
        qnt_bal = deposit()
        atualizar_balance(USER, qnt_bal, "add")
        loading(50, "Depositando")
        print(color("Deposito feito com sucesso!","lgreen"))
        sleep(2)
        print(text_menu_principal())
        sleep(2)
    
    #!  Chama a função do saque.
    elif option == "B":
        loading(30, "Carregando opção SAQUE")
        while True:
            try:
                qnt_wd = withdraw()
                if qnt_wd == 0:
                    raise Exception(insufficient_balance())
                else:
                    atualizar_balance(USER, qnt_wd, "rem")
                    loading(50, "Sacando")
                    print(color("Saque feito com sucesso!","lgreen"))
                    sleep(2)
                    print(text_menu_principal())
                    sleep(2)
                    break
            except Exception as e:
                loading(30, "Processando")
                print(f"Ocorreu um erro ao fazer o saque: {e}")
                sleep(2)
                print(text_menu_principal())
                sleep(2)
    
    #!  Chama a função do menu de extras
    elif option == "C":
        loading(30, "Carregando menu de extras")
        funcionalidades.extras.main_extras.main_extras_menu()

    #!  Sair do programa
    elif option == "X":
        loading(30, "Encerrando programa...")
        titulos("PROGRAMA ENCERRADO!")
        quit()
    menu_principal(USER)


#!  Programa principal
if __name__ == "__main__":
    run()