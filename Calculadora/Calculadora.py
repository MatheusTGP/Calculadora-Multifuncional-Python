import time
print('======[ Menu_Inicial ]======')
valor1 = int(input("[ Valor1 ]: "))
time.sleep(1)
valor2 = int(input("[ Valor2 ]: "))
time.sleep(1)
print(" ")
print(' Calculando Soma... ')
print(" ")
# Calcular Resultados pela Máquina
sun1 = valor1 + valor2
sun2 = valor1 - valor2
sun3 = valor1 * valor2
# Executar Resultado
print('====| Resultados |====')
print('{} + {} = [ {} ] \n {} - {} = [ {} ] \n {} × {} = [ {} ] \n '.format(valor1, valor2, sun1, valor1, valor2, sun2, valor1, valor2, sun3))
print('====| Calculos |====')
# Fim do Código, programa não executa automáticamente novamemte..
