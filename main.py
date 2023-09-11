###################################################################################################

from time import sleep

###################################################################################################

#TODO                           imports da pasta do programa

#?  CONFIG_PROGRAM
from config_program.main_balance import update_balance, lerBalance
from config_program.main_text import *
from config_program.config_informations_user import *
from config_program.config import *

#?  FUNCIONALIDADES
from funcionalidades.transacoes_bancarias.main_transactions import *
import funcionalidades.extras.main_extras

###################################################################################################


#!  Mostrar menu principal
class MainBankAccount():
    def __init__(self):
        self.archive_name = "user_info.txt"
        self.money_file = "money_user.txt"
    
    
    def run(self):
        if not criarArquivo(self.archive_name):
            titulos("CADASTRAR NOVO USUÁRIO")
            name = str(input("Digite seu nome: "))
            username = gerarUser(name)
            token = gerarToken()
            account = gerarNumeroConta()
            loading(30, "Criando arquivo do usuário!")
            cadastrarInformacoes(self.archive_name, username, token, account)
            if not criarArquivo(self.money_file):
                loading(15, "Criando arquivo de dinheiro!")
                cadastrarMoney(self.money_file, 0)
            if login_user():
                self.menu_principal()
            else:
                print(color("Número te tentativas excedido! Fechando programa por segurança!","red"))
        else:
            titulos("ÁREA DE LOGIN")
            if login_user():
                self.menu_principal()
            else:
                print(color("Número te tentativas excedido! Fechando programa por segurança!","red"))
                
                
    def menu_principal(self):
        """Mostra o menu principal junto a função actual_balance_str()
        """
        titulos("SEJA BEM VINDO AO MENU PRINCIPAL DO BANCO NSX")
        print(self.actual_balance_str())
        loading(30, "Carregando menu de opções")
        self.menu_options()


    #!  Mostrar saldo disponivel
    def actual_balance_str(self):
        """Formata o saldo atual em string para mostrar corretamente o valor monetário.

        Returns:
            STRING: Retorna a frase SALDO DISPONÍVEL junto ao saldo ja formatado para a região pt-BR
        """
        print()
        import locale
        locale.setlocale(locale.LC_ALL, 'pt-BR')
        balance_actual = lerBalance()
        balance_actual = round(balance_actual, 2)
        balance_actual_str = locale.format_string("%.2f", balance_actual, grouping=True)
        actual_balance = color("Saldo disponível: R$ ","l_g")+color(balance_actual_str, "lwhite")
        return actual_balance


    #!  Mostrar opções do menu principal
    def menu_options(self):
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
            update_balance(qnt_bal, "add")
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
        self.menu_principal()


#!  Programa principal
if __name__ == "__main__":
    MainBankAccount().run()