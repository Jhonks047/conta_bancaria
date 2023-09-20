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
#TODO   | LEGENDA DAS MARCAÇÕES
# [x] Tarefa concluída
# [o] Tarefa em andamento
# [ ] Tarefa ainda não foi começada

#!  [x] Alterar o run() para salvar os dados em um banco de dados ao invés de criar arquivos.
#!  [o] Salvar dados monetários, bilhetes e criptomoedas no banco de dados.
#!  [ ] 
#?  [ ] Criar uma interface de cadastro e login de usuário mais detalhada.
#?  [ ] Ajustar as telas de loading com outras informações e visivelmente mais agradável.

###################################################################################################


#!  Mostrar menu principal

def run():
    global USER
    titulos("BANCO MKL | ÁREA DO USUÁRIO")
    print(f"""
Olá! Seja bem-vindo(a) ao banco MKL!

Escolha uma das seguintes opções:
        
        {color("[ A ] Fazer login", "lcyan")}
        {color("[ B ] Cadastrar-se", "lgreen")}
        
    {color("[ X ] Sair do programa", "lred")}
    """)
    choice = choices("A", "B", "X")
    if choice == "A":
        contador = 3
        while contador > 0:
            try:
                user = fazer_login()
                USER = user.uid
                if user:
                    print("Login efetuado com sucesso!")
                    break
            except:
                contador -= 1
                print(color(f"{contador} tentativas restantes", "lred"))
                continue
        if contador == 0:
            print("Excedeu o limite, fechando programa por segurança!")
            quit()
    elif choice == "B":
        while True:
            try:
                titulos("CADASTRAMENTO DE USUÁRIO")
                name = str(input("Digite seu nome: ")).capitalize().strip()
                password = str(input("Digite uma senha para o cadastro: ")).strip()
                username = gerarUser(name)
                uid = gerar_uid(username)
                email = gerar_email(name)
                numero_da_conta = gerarNumeroConta()
                criar_usuario(email=email, senha=password, uid=uid)
                criar_informacoes(uid, numero_da_conta=numero_da_conta)
            except:
                continue
            else:
                contador = 3
                while contador > 0:
                    try:
                        user = fazer_login()
                        USER = user.uid
                        if user:
                            print("Login efetuado com sucesso!")
                            break
                    except:
                        contador -= 1
                        print(color(f"{contador} tentativas restantes", "lred"))
                        continue
                if user:
                    break
                if contador == 0:
                    print("Excedeu o limite, fechando programa por segurança!")
                    quit()
                menu_principal(USER=USER)
            
def menu_principal(USER):
    """Mostra o menu principal junto a função actual_balance_str()
    """
    titulos("SEJA BEM VINDO AO MENU PRINCIPAL DO BANCO MKL")
    actual_balance_str(USER=USER), pegar_informacoes_database(USER=USER, sit="conta_bancaria")
    menu_options(USER=USER)


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
    print(f"""
        {color("[ A ] Realizar Depósito", "green")}
        {color("[ B ] Relizar Saque", "yellow")}
        {color("[ C ] Abrir menu de Extras", "magenta")}
        
    {color("[ X ] Fechar programa", "lred")}
    """)
    option = choices("A", "B", "C", "X")
    
    #!  Chama a função do depósito.
    if option == "A":
        qnt_bal = deposit()
        atualizar_balance(USER=USER, amount=qnt_bal, sit="add")
        print(color("Deposito feito com sucesso!","lgreen"))
    
    #!  Chama a função do saque.
    elif option == "B":
        while True:
            try:
                qnt_wd = withdraw(USER=USER)
                if not qnt_wd:
                    raise Exception(insufficient_balance())
                else:
                    atualizar_balance(USER=USER, amount=qnt_wd, sit="rem")
                    print(color("Saque feito com sucesso!","lgreen"))
                    break
            except Exception as e:
                print(f"Ocorreu um erro ao fazer o saque: {e}")
    
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