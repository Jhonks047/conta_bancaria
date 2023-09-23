###################################################################################################
#TODO                           Outros imports

###################################################################################################

#TODO                           Imports da pasta do programa

import tools.extras.main_extras
from config.get_informations import *
from config.informations_user import *
from config.main_balance import *
from config.main_text import *
from config.validar_login import *
from tools.transacoes_bancarias.main_transactions import *

###################################################################################################

#TODO                              COISAS A FAZER
#TODO   | LEGENDA
#!  | Importante *
#?  | Otimização | Ajustar
#*  | Criação
#TODO   | LEGENDA DAS MARCAÇÕES
# [x] Tarefa concluída
# [o] Tarefa em andamento
# [ ] Tarefa ainda não foi começada

#!  [x] Alterar o run() para salvar os dados em um banco de dados ao invés de criar arquivos.
#!  [o] Salvar dados monetários, bilhetes e criptomoedas no banco de dados.
#!  [o] Criar a documentação completa de todo o programa bem detalhada para outros desenvolvedores.
#?  [o] Criar uma interface de cadastro e login de usuário mais detalhada.
#?  [ ] Ajustar as telas de loading com outras informações e visivelmente mais agradável.
#?  [o] Substituir algumas palavras em inglês para português.
#*  [ ] Criar a criptomoeda Ethereum.
#*  [ ] Criar o inventário que mostre todas as criptomoedas do usuário no menu de criptomoedas.
#*  [ ] Criar opção de de cartão de crédito.
#*  [ ] Criar um arquivo para lidar somente com tratamento de erros utilizando decoradores
#*  [ ] 

###################################################################################################

def login_usuario():
    tentativas = 3
    while tentativas > 0:
        try:
            user = fazer_login()
            USER = user.uid
            if user:
                print("Login efetuado com sucesso!")
                break
        except:
            tentativas -= 1
            print(color(f"{tentativas} tentativas restantes", "lred"))
    if tentativas == 0:
        print("Excedeu o limite, fechando programa por segurança!")
        quit()
    return USER
        

def cadastrar_usuario():
    while True:
        try:
            titulos("CADASTRAMENTO DE USUÁRIO")
            name = str(input("Digite seu nome: ")).capitalize().strip()
            password = str(input("Digite uma senha para o cadastro: ")).strip()
            username = gerarUser(name)
            uid = gerar_uid(username)
            email = gerar_email(uid)
            numero_da_conta = gerarNumeroConta()
            criar_usuario(email=email, senha=password, uid=uid, name=name)
            criar_informacoes(uid, numero_da_conta=numero_da_conta, name=name)
        except:
            continue
        else:
            USER = login_usuario()
            return USER


def run():
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
        USER = login_usuario()
        if USER:
            menu_principal(USER=USER)
    elif choice == "B":
        USER = cadastrar_usuario()
        if USER:
            menu_principal(USER=USER)
#!  Mostrar menu principal
def menu_principal(USER):
    """Mostra o menu principal junto a função actual_balance_str()
    """
    titulos(f"SEJA BEM VINDO AO MENU PRINCIPAL DO BANCO MKL")
    nome_usuario = pegar_informacoes_database(USER=USER, sit="nome")
    print(f"{'Usuário logado: '}{nome_usuario} | UID: {USER}")
    actual_balance_str(USER=USER)
    pegar_informacoes_database(USER=USER, sit="conta_bancaria")
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
    print()
    print(color("       MENU DE OPÇÕES", "lred"))
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
        tools.extras.main_extras.main_extras_menu(USER=USER)

    #!  Sair do programa
    elif option == "X":
        loading(30, "Encerrando programa...")
        titulos("PROGRAMA ENCERRADO!")
        quit()
    menu_principal(USER)


#!  Programa principal
if __name__ == "__main__":
    run()