# Desafio 1 – Operadores
# Tendo como dados de entrada a altura de uma pessoa
# Construa um algoritmo que calcule seu peso ideal,
# usando a seguinte fórmula: (72.7*altura) – 58.

altura = float(input('Digite a sua altura [m]: '))
pesoideal = (72.7 * altura) - 58
print(f'O seu peso ideal é {pesoideal:.2f} kg.')
