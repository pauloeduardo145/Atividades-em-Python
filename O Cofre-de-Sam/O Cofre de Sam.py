# Criando uma lista vazia
numero = []
contador = 0

# pedir numero
for i in range(5):
    valor = int(input(f'{i}ª numero: '))
    numero.append(valor)
    if valor % 2 == 0:
        contador += 1

#numeros escrito pelo usuario
print(numero)

#maior numero digitado
maior_numero = max(numero)
print("O maior numero é ", maior_numero)

#total
total = sum(numero)
print("Soma total: ",total)

#quantidade de par
print(f"Quantidade de pares: {contador}") 

#o programa deve exibir uma mensagem
def eum():
    if total > 50:
        print("Cofre aberto.")
    else:
        print(f"A sequência falhou.")

eum()
