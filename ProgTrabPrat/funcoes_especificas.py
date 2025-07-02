''' Crie uma função chamada “retorna_meses” em fne, que receberá um número de 1 a 12 (em 
números) e retornará o nome do mês por extenso. Caso o valor não corresponda a algum mês, deverá ser 
retornado “Entrada Inválida”.'''

def retorna_meses(numero):
    if numero == 1:
        print("Janeiro")
    elif numero == 2:
        print("Fevereiro")
    elif numero == 3:
        print("Março")
    elif numero == 4:
        print("Abril")
    elif numero == 5:
        print("Maio")
    elif numero == 6:
        print("Junho")
    elif numero == 7:
        print("Julho")
    elif numero == 8:
        print("Agosto")
    elif numero == 9:
        print("Setembro")
    elif numero == 10:
        print("Outubro")
    elif numero == 11:
        print("Novembro")
    elif numero == 12:
        print("Dezembro")
    else:
        print("Entrada Inválida")

'''Crie uma função “expressoes_fn” em fne calcule e exiba a equação e também o valor da 
resposta de cada expressão abaixo: 
a) (20 - 15)/2   
e) 23 div 4   
b) 20 - 15/2  
f) 23 mod 4  
c) 2*5/20 + 30/15*2 
d) 2*(5/20) + 30/(15*2)'''

def expressoes_fn():
    print("a) (20 - 15)/2 =", (20 - 15)/2)
    print("b) 20 - 15/2 =", 20 - 15/2)
    print("c) 2*5/20 + 30/15*2 =", 2*5/20 + 30/15*2)
    print("d) 2*(5/20) + 30/(15*2) =", 2*(5/20) + 30/(15*2))
    print("e) 23 div 4 =", 23 // 4)
    print("f) 23 mod 4 =", 23 % 4)

'''Crie uma função “numero_N” no fne que deverá receber por parâmetro um número N e 
imprima na tela “F0”,“F1”, “F2” ou “F3”, conforme a condição: 
• “F0”, se N <=0 
• “F1”, se N >0 e N <= 10 
• “F2”, se N > 10 e N <= 100  
• “F3”, se n > 100 '''

def numero_N(n):
    if n <= 0:
        print("F0")
    elif n > 0 and n <= 10:
        print("F1")
    elif n > 10 and n <= 100:
        print("F2")
    else:
        print("F3")

'''Crie uma função “par_impar” no fne que receba um valor por parâmetro e retorna True ou 
False, dependendo se o número é par ou ímpar. O programa principal deverá imprimir na tela se é par ou 
ímpar.'''

def par_impar(valor):
    if valor % 2 == 0:
        print(valor, "é Par")
    else:
        print(valor, "é Ímpar")
