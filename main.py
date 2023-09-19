import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("C:\Users\jhona\OneDrive\Documentos\MeusProjetos\conta_bancaria\token\conta-bancaria-mkl-firebase-adminsdk-qxtvi-b80bb839e2.json")
firebase_admin.initialize_app(cred)

###################################################################################################
#TODO                           Outros imports
from time import sleep

###################################################################################################

#TODO                           Imports da pasta do programa

#?  CONFIG_PROGRAM
from config_program.main_balance import update_balance, lerBalance
from config_program.main_text import *
from config_program.config_informations_user import *
from config_program.config import *

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
    if not verificar_users():
        titulos("CADASTRAR NOVO USUÁRIO")
        name = str(input("Digite seu nome: ")).capitalize().strip()
        username = gerarUser(name)
        token = gerarToken()
        account = gerarNumeroConta()
        loading(30, "Adicionando ao banco de dados")
        if cadastrarInformacoes(name, username, token, account):
            status, USER = validarLogin()
            if status:
                menu_principal(USER)
            else:
                print(color("Número de tentativas excedido! Fechando programa por segurança!","red"))
        else:
            print("ERRO!")
    else:
        status, USER = validarLogin()
        if status:
            menu_principal(USER)
        else:
            print(color("Número de tentativas excedido! Fechando programa por segurança!","red"))
            
            
def menu_principal(USER):
    """Mostra o menu principal junto a função actual_balance_str()
    """
    titulos("SEJA BEM VINDO AO MENU PRINCIPAL DO BANCO NSX")
    print(actual_balance_str(USER))
    loading(30, "Carregando menu de opções")
    menu_options(USER)


#!  Mostrar saldo disponivel
def actual_balance_str(USER):
    """Formata o saldo atual em string para mostrar corretamente o valor monetário.

    Returns:
        STRING: Retorna a frase SALDO DISPONÍVEL junto ao saldo ja formatado para a região pt-BR
    """
    print()
    import locale
    locale.setlocale(locale.LC_ALL, 'pt-BR')
    balance_actual = lerBalance(USER)
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
        update_balance(USER, qnt_bal, "add")
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
                if qnt_wd > update_balance() or qnt_wd == 0:
                    raise Exception(insufficient_balance())
                else:
                    update_balance(qnt_wd, "rem")
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
    menu_principal()


#!  Programa principal
if __name__ == "__main__":
    run()