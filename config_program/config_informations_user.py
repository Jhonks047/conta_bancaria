import string
import random
from config_program.config import color
from config_program.main_text import *



def gerarUser(name):
    prefix = name[:3].lower()
    allowed = string.ascii_lowercase+string.digits
    suffix = "".join(random.choices(allowed, k=3))
    user_name = prefix+suffix
    return user_name


def gerar_uid(username):
    prefix = username[:4].lower()
    allowed = string.ascii_lowercase+string.digits
    suffix = "".join(random.choices(allowed, k=7))
    uid = prefix+suffix
    return uid


def gerarNumeroConta():
    allowed = string.digits
    num = "".join(random.choices(allowed, k=12))
    num = f"{num[:3]}.{num[3:7]}.{num[7:10]}-{num[10:]}"
    return num


def gerar_email(name):
    prefix = name[:3]
    sufix = '@mkl.bank'
    email = prefix + sufix
    return email