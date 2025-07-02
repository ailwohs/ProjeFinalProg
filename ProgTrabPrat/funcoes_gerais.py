'''Crie duas funções em fng  chamadas “inicio_prog” e “fim_prog”. A primeira deve imprimir na 
tela um cabeçalho para o seu programa com a mensagem “Bem vindo <SEU NOME>”, e a segunda 
imprimir uma mensagem de despedida “Até logo <SEU NOME>” . Estilize suas mensagens com traços, ‘#’, 
“=”, enfim, use sua criatividade e “senso de estilo”. As funções, obvio, devem ser chamadas ao iniciar o 
programa e ao encerrá-lo. '''

def inicio_prog():
    print("#" * 40)
    print("Bem vindo", "Julia Renata Soares")
    print("#" * 40)

def fim_prog():
    print("=" * 40)
    print("Até logo", "Julia Renata Soares")
    print("=" * 40)

'''Crie uma função “somatório” no fng que receba por parâmetro um valor inteiro qualquer e 
retorne o somatório de todos os valores até aquele número. Exemplo: a função recebe 10, ele tem que 
calcular o valor de 10+9+8+7+6+5+4+3+2+1 e retornar esse valor. '''

def somatorio(n):
    soma = 0
    i = 1
    while i <= n:
        soma = soma + i
        i = i + 1
    print("Somatório até", n, "é", soma)
    
'''Crie uma função “somatório” no fng que receba por parâmetro um valor inteiro qualquer e 
retorne o somatório de todos os valores até aquele número. Exemplo: a função recebe 10, ele tem que 
calcular o valor de 10+9+8+7+6+5+4+3+2+1 e retornar esse valor. '''    

def media_somatorio(n):
    soma = 0
    i = 1
    while i <= n:
        soma = soma + i
        i = i + 1
    media = soma / n
    print("Média do somatório até", n, "é", media)

''' Crie uma função “operacoes_mat” no fng que receba dois valores por parâmetro e retorne a 
soma,  a subtração a multiplicação e a divisão inteira e resto da divisão. Estes valores deverão ser 
impressos na tela pelo programa principal. '''

def operacoes_mat(a, b):
    soma = a + b
    sub = a - b
    mult = a * b
    div_int = a // b
    resto = a % b
    print("Soma:", soma)
    print("Subtração:", sub)
    print("Multiplicação:", mult)
    print("Divisão inteira:", div_int)
    print("Resto da divisão:", resto)
