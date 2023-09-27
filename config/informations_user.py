import random
import string


def gerarUser(name: str):
    """GERA O USERNAME DO USUÁRIO COM BASE NO NOME INFORMADO

    Args:
        name ( STR ): Utilizado para gerar um username com digitos e letras aleatórios

    Returns:
        STR: Retorna o username gerado com letras e dígitos
    """
    prefix = name[:3].lower()
    allowed = string.ascii_lowercase+string.digits
    suffix = "".join(random.choices(allowed, k=3))
    user_name = prefix+suffix
    return user_name


def gerar_uid(username: str):
    """GERA O UID DO USUÁRIO

    Args:
        username ( STR ): utilizado para criar o uid do usuário com base no username gerado pelo < gerarUser >

    Returns:
        STR: Retorna o UID gerado com 7 caracteres incluindo letras e dígitos.
    """
    prefix = username[:4].lower()
    allowed = string.ascii_lowercase+string.digits
    suffix = "".join(random.choices(allowed, k=7))
    uid = prefix+suffix
    return uid


def gerarNumeroConta():
    """Gera o número da conta do usuário de forma aleatória

    Returns:
        STR: Retorna o número da conta do usuário.
    """
    allowed = string.digits
    num = "".join(random.choices(allowed, k=12))
    num = f"{num[:3]}.{num[3:7]}.{num[7:10]}-{num[10:]}"
    return num


def gerar_email(uid: str):
    """Gera um email para o login do usuário contendo o UID + @mkl.bank

    Args:
        uid ( STR ): uid gerada pela função < gerar_uid > que será usada para criar o email do usuário

    Returns:
        STR: Retorna o UID do usuário + o @mkl.bank
    """
    prefix = uid
    sufix = '@mkl.bank'
    email = prefix + sufix
    return email