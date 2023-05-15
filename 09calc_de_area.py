# exercício 9: Desenvolva um programa que leia a largua e altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária
# p/ pintá-la. Cada litro de tinta pinta uma área de 2m²

larg = float(input('Largura em m: '))
alt = float(input('Altura em m: '))
print('O cálculo de sua área é: {}m² e a quantidade de tinta necessária para pintá-la é: {}'. format((larg*alt), (larg*alt/2)))
