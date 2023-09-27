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
#!  [x] Salvar dados monetários e criptomoedas no banco de dados.
#!  [o] Criar a documentação completa de todo o programa bem detalhada para outros desenvolvedores.
#?  [o] Criar uma interface de cadastro e login de usuário mais detalhada.
#?  [ ] Ajustar as telas de loading com outras informações e visivelmente mais agradável.
#?  [o] Substituir algumas palavras em inglês para português.
#?  [o] Arrumar todas as funções do jogo MIXy
#*  [ ] Criar a criptomoeda Ethereum.
#*  [ ] Criar o inventário que mostre todas as criptomoedas do usuário no menu de criptomoedas.
#*  [ ] Criar opção de cartão de crédito.
#*  [ ] Criar um arquivo para lidar somente com tratamento de erros utilizando decoradores
#*  [ ] Criar transferências bancárias entre contas salvas na database

###################################################################################################


def login_usuario():
    """ÁREA DE LOGIN DO USUÁRIO
        Essa função faz o login do usuario chamando outra função para validar com os dados do banco de dados.
    
    RETURN:
        Essa função retorna o USER, que nada mais é do que o user.uid que é gerado aleatoriamente em outra função
        que será usado posteriormente para validar transações bancárias e etc.
    """

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
    """CADASTRAMENTO DE USUÁRIOS
        Essa função faz o cadastro dos usuários utilizando o nome que o usuário informar, chamando outras funções como:
        < gerarUser > Serve para pegar o nome que o usuário informou, pegando as 3 primeiras letras.
        < gerar_uid > Função para pegar o username gerado pela função anterior e cria seu UID.
        < gerar_email > Função para pegar o uid do usuário gerado pela função anterior e acrescentando @mkl.bank.
        < gerarNumeroConta > Função para gerar um número aleatório da conta bancária do usuário.

    RETURN:
        Caso o cadastro do usuário ter êxito, o USER irá chamar a função de < login_usuario > e irá armazenar o UID
        e irá retornar o USER.
    """

    while True:
        try:
            titulos(msg="CADASTRAMENTO DE USUÁRIO", cor="lgreen")
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
    """CHAMAR A ÁREA DO USUÁRIO
        Essa função chama a área do usuário para efetuar o login ou se cadastrar, contendo as seguintes opções:
        
        >> [ A ] Fazer login
        >> [ B ] Cadastrar-se
        >> [ X ] Sair do programa
    """

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


#  Mostrar menu principal
def menu_principal(USER: str):
    """Função para mostrar o menu principal junto as seguintes funções:
    
        nome_usuario = < pegar_informacoes_database > Pegar o nome do usuário e armazenar na variável < nome_usuario > e mostrar no menu.
    
        < actual_balanced_str > Pega o dinheiro do usuário e mostra no menu totalmente formatado em BRL > R$0,00 <
    
        < pegar_informacoes_database > Aqui a função mostra no menu a conta bancária do usuário.
    
        < menu_options > Chama o menu de opções do menu principal.
    
    Args:
        USER ( STR ): Usuário atual logado no sistema
    """
    
    titulos(f"SEJA BEM VINDO AO MENU PRINCIPAL DO BANCO MKL")
    nome_usuario = pegar_informacoes_database(USER=USER, sit="nome")
    print(f"{'Usuário logado: '}{nome_usuario} | UID: {USER}")
    actual_balance_str(USER=USER)
    pegar_informacoes_database(USER=USER, sit="conta_bancaria")
    menu_options(USER=USER)


#  Mostrar opções do menu principal
def menu_options(USER: str):
    """Menu de opções bancárias
        Essa função realiza transações bancárias de acordo com a escolha do usuário.
        Dentro de cada escolha do usuário há uma função que será chamada, as escolhas do usuário são as seguintes:
            >   [ A ]   Realizar Depósito
            >   [ B ]   Realizar Saque < atualmente desabilitado >
            >   [ C ]   Abrir menu de Extras
            >   [ X ]   Fechar programa
    
    Args:
        USER ( STR ): Usuário atual logado no sistema
    """
    
    print()
    print(color("     MENU DE OPÇÕES", "lred"))
    print(f"""
        {color("[ A ] Realizar Depósito", "green")}
        {color("[ B ] Relizar Saque < atualmente desabilitado >", "white")}
        {color("[ C ] Abrir menu de Extras", "magenta")}
        
    {color("[ X ] Fechar programa", "lred")}
    """)
    option = choices("A", "B", "C", "X")
    
    #  Chama a função do depósito.
    if option == "A":
        qnt_bal = deposit()
        atualizar_balance(USER=USER, amount=qnt_bal, sit="add")
        print(color("Deposito feito com sucesso!","lgreen"))
    
    #  Chama a função do saque.
    elif option == "Z":
        pass
    
    #  Chama a função do menu de extras
    elif option == "C":
        tools.extras.main_extras.main_extras_menu(USER=USER)

    #  Sair do programa
    elif option == "X":
        loading(30, "Encerrando programa...")
        titulos(msg="PROGRAMA ENCERRADO!", cor="red")
        quit()
    menu_principal(USER)


#  Programa principal
if __name__ == "__main__":
    run()