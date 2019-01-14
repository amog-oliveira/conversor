#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

extenso = [
  {1:"um", 2:"dois", 3:"três", 4:"quatro", 5:"cinco", 6:"seis", 7:"sete", 8:"oito", 9:"nove", 10:"dez", 11:"onze", 12:"doze",
  13:"treze", 14:"quatorze", 15:"quinze", 16:"dezesseis", 17:"dezessete", 18:"dezoito", 19:"dezenove"},
  {2:"vinte", 3:"trinta", 4:"quarenta", 5:"cinquenta", 6:"sessenta", 7:"setenta", 8:"oitenta", 9:"noventa"},
  {1:"cento", 2:"duzentos", 3:"trezentos", 4:"quatrocentos", 5:"quinhentos", 6:"seissentos", 7:"setessentos", 
  8:"oitocentos", 9:"novecentos"}
]

unidade = ['', ' mil', (' milhão', ' milhões'), (' bilhão', ' bilhões'), (' trilhão', ' trilhões')]

def centenas(valor, posicao):
    valor = '0' * (3 - len(valor)) + valor 

    if valor == '000':
        return ''
    if valor == '100':
        return 'cem'
    array_extenso = ''
    dezena = valor[1] + valor[2] 
    if valor[0] != '0':
        array_extenso += extenso[2][int(valor[0])]
        if dezena != '00':
            array_extenso +=  ' e '
        else:
            return array_extenso + (type(unidade[posicao]) == type(()) and (int(valor) > 1 and unidade[posicao][1] or unidade[posicao][0]) or unidade[posicao])
    if int(dezena) < 20:
        array_extenso += extenso[0][int(dezena)]
    else:
        if valor[1] != '0':
            array_extenso += extenso[1][int(valor[1])]
        if valor[2] != '0':
            array_extenso += ' e ' + extenso[0][int(valor[2])]
    return array_extenso + (type(unidade[posicao]) == type(()) and (int(valor) > 1 and unidade[posicao][0]) or unidade[posicao])

def extenso_reais(reais_valor, centavos_valor):
    array_extenso = []
    posicao = 0

    if(int(centavos_valor) == 0):
        array_extenso.append('zero centavos')
    elif(int(centavos_valor) == 1):
        array_extenso.append('um centavo')
    else:
        array_extenso.append(centenas(centavos_valor,0) + ' centavos')
    
    if(int(reais_valor) == 0):
        array_extenso.append('zero reais')
        array_extenso.reverse()
        return ' e '.join([resultado for resultado in array_extenso if resultado])
    elif(int(reais_valor) == 1):
        array_extenso.append('um real')
        array_extenso.reverse()
        return ' e '.join([resultado for resultado in array_extenso if resultado])
    while reais_valor:
        valor_em_reais = reais_valor[-3:]
        reais_valor = reais_valor[:-3]
        if (posicao == 0):
            array_extenso.append(centenas(valor_em_reais, posicao) + ' reais')
        else:
            array_extenso.append(centenas(valor_em_reais, posicao))
        posicao += 1
    array_extenso.reverse()
    return ' e '.join([resultado for resultado in array_extenso if resultado])

if __name__ == '__main__':
  digitos = sys.argv[1]
  try:
    digito_reais, digito_centavos = digitos.split(',')
  except:
    print ('Erro ao ler o valor.')
  if(len(digito_centavos) != 2):
    print ('O valor está incorreto na casa dos centavos.')
    sys.exit(1)
  print (digitos)
  print (extenso_reais(digito_reais,digito_centavos))