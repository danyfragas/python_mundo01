# exercício 10: Desenvolva um programa que leia o preço de um produto e mostre o seu novo preço com 5% de desconto.

val = float(input('Informe o valor: R$ '))
print('O preço R$ {} com 5% de desconto é: R$ {:.2f}'. format(val, (val-(val*(5/100)))))
# =================================

# exercício 11: Desenvolva um programa que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento

sal = float(input('Informe o salário: R$ '))
print('O seu salário terá um aumento de 15%. Assim, o seu novo salário será: R$ {:.2f}'. format(sal+(sal*(15/100))))
