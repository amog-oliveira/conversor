#!/usr/bin/python
# -*- coding: utf-8 -*-

unidade = {'0': 'zero', '1': 'um', '2': 'dois', '3': 'três', '4': 'quatro', '5': 'cinco', '6': 'seis', '7': 'sete', '8': 'oito', '9': 'nove'}
dez = {'10': 'dez', '11': 'onze', '12': 'doze', '13': 'treze', '14': 'catorze', '15': 'quinze', '16': 'dezesseis', '17': 'dezessete', '18': 'dezoito', '19': 'dezenove'}
dezena = {'2': 'vinte', '3': 'trinta', '4': 'quarenta', '5': 'cinquenta', '6': 'sessenta', '7': 'setenta', '8': 'oitenta', '9': 'noventa'}
milhar = {'3': 'cem', '4': 'mil', '5': 'milhão(ões)', '6': 'bilhão(ões)', '7': 'trilhão(ões)'}

def pegar_valor():
    valor = input('Digite um preço (ex.:1,00):')
    try:
        reais, centavos = valor.split(',')
    except BaseException as e:
        print('O valor inserido não está correto')
        raise(e)   

    return (reais,centavos)

def pegar_centavos(centavos):
    if centavos[0] != '0':
        if centavos in dez:
            centavos = f'{dez[centavos]} centavo(s)'
        else:
            centavos = f'{dezena[centavos[0]]} e {unidade[centavos[1]]} centavo(s)'
    else:
        centavos = f'{unidade[centavos[1]]} centavo(s)'         

    return centavos

def pegar_dezena(digitos):
    if digitos in unidade:
        digitos = f'{unidade[digitos]} real (is)'
    elif digitos in dez:
        digitos = f'{dez[digitos]} real (is)'
    else:
        digitos = f'{dezena[digitos[0]]} e {unidade[digitos[1]]} real(is)'
        
    return digitos

def pegar_unity(valor):
    return milhar[len(valor)]

if __name__ == '__main__':
    valores = pegar_valor()
    digitos = pegar_dezena(valores[0])
    centavos = pegar_centavos(valores[1])
    print(f'{digitos} e {centavos}')
