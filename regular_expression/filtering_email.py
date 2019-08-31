#!/usr/bin/env python3

import re

regex = re.compile(r'([a-zA-Z0-9._%+-]+)@([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})')

def validar_email(email):
    matches = regex.search(email)

    if matches is None:
        email_valido, endereco, dominio = False, None, None
    else:
        email_valido, endereco, dominio = True, matches.group(1), matches.group(2)
    return email_valido, endereco, dominio

def ocultar(regex, email):
    return regex.sub("******",email)
        
if __name__ == "__main__":
    emails = ['desconhecido@hotmail.com','teste.teste@outlook.com','teste-teste@gov.edu','teste.teste','@gmail.com','google.com']

    for email in emails:
        msg = 'Email {}'.format(email)
        e_valido, _ , dominio = validar_email(email)
        if e_valido:
            print('Email {} e valido e pertence ao dominio {}'.format(email,dominio))
        else:
            print('Email {} nao e valido'.format(email))

    usuarios_ocultados = list()
    regex_usuario = re.compile(r'teste(\.|-)teste')
    for email in emails:
        usuarios_ocultados.append(ocultar(regex_usuario,email))
    print("Lista de emails  {}".format(usuarios_ocultados))