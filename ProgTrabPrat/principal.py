import funcoes_gerais as fng
import funcoes_especificas as fne


'''Crie um menu que apresente as seguintes opções ao usuário: 
Escolha uma das opções: 
S ou 0 - Sair 
M ou 1 - Meses  
E ou 2 - Expressões Matemáticas 
F ou 3 - F0, F1, F2 ou F3 
A ou 4 - Somatório 
H ou 5 - Média de valores 
P ou 6 - Par ou Ímpar 
X ou 7 -  
OBS: no caso das letras, podem ser letras maiúsculas ou minúsculas. Por exemplo: se digitar “s”, “S” ou 0 o 
efeito precisa ser o mesmo '''
fng.inicio_prog()

while True:
    print("\nEscolha uma das opções:")
    print("S ou 0 - Sair")
    print("M ou 1 - Meses")
    print("E ou 2 - Expressões Matemáticas")
    print("F ou 3 - F0, F1, F2 ou F3")
    print("A ou 4 - Somatório")
    print("H ou 5 - Média de valores")
    print("P ou 6 - Par ou Ímpar")
    print("X ou 7 - Operações Matemáticas")

    op = input("Digite sua opção: ")

    if op == "S" or op == "s" or op == "0":
        fng.fim_prog()
        break

    elif op == "M" or op == "m" or op == "1":
        num = int(input("Digite um número de 1 a 12: "))
        fne.retorna_meses(num)

    elif op == "E" or op == "e" or op == "2":
        fne.expressoes_fn()

    elif op == "F" or op == "f" or op == "3":
        n = int(input("Digite um número: "))
        fne.numero_N(n)

    elif op == "A" or op == "a" or op == "4":
        n = int(input("Digite um número inteiro: "))
        fng.somatorio(n)

    elif op == "H" or op == "h" or op == "5":
        n = int(input("Digite um número: "))
        fng.media_somatorio(n)

    elif op == "P" or op == "p" or op == "6":
        valor = int(input("Digite um número: "))
        fne.par_impar(valor)

    elif op == "X" or op == "x" or op == "7":
        a = int(input("Digite o primeiro número: "))
        b = int(input("Digite o segundo número: "))
        fng.operacoes_mat(a, b)

    else:
        print("Opção inválida.")
