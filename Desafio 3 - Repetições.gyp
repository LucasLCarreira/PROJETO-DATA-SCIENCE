# A série de Fibonacci é formada pela sequência 1,1,2,3,5,8,13,21,34,55,...
# Faça um programa capaz de gerar a série até o n−ésimo termo.
# Qual número você deseja receber a sequencia Fibonacci? 34

n = int(input('Digite um número: '))
a = 0
b = 1
c = 0
while c < n:
    c = c + a
    a = b
    b = c
    print(c,end=' ')
