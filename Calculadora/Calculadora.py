# @Autor: MatheusTGamerPro
# @GitHub: https://github.com//MatheusTGamerPro
# @100% Python

import time
print('======[ Menu_Inicial ]======')
valor1 = int(input("[ Valor1 ]: "))
time.sleep(0)
valor2 = int(input("[ Valor2 ]: "))
time.sleep(1)
print(" ")
print(' Calculando... ')
print(" ")
# Calcular Resultados pela Máquina
sun1 = valor1 + valor2
sun2 = valor1 - valor2
sun3 = valor1 * valor2
sun4 = valor1 / valor2
# Executar Resultado
print('====| Resultados |==== \n')
print(' [ {} + {} ] = [ {} ] \n [ {} - {} ] = [ {} ] \n [ {} × {} ] = [ {} ] \n [ {} ÷ {} ] = [ {} ] \n'.format(valor1, valor2, sun1, valor1, valor2, sun2, valor1, valor2, sun3, valor1, valor2, sun4))
print('====| Calculos |====')
# Fim do Código, programa não executa automáticamente novamemte..
