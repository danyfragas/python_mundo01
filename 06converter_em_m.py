# exercício 6: Desenvolva um programa que leia um valor em metros e converta em cm e mm km hm dam m dm cm mm

v = float(input('Valor em metros: '))
print('O valor em dm  é {}, em cm é {} e mm é {}'. format((v*10), (v*100), (v*1000)))
print('O valor em km é: {}, em hm é: {}, em dam é: {} '. format((v/1000), (v/100), (v/10)))
