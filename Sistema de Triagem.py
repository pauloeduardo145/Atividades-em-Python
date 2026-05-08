#Idades
idades = []


#Pedido para digitar oito idades diferentes

for i in range(8):
    valor = int(input(f'{i + 1}ª idade '))
    idades.append(valor)

# mostrar idades
print("As idades digitadas são ",idades)

#para cada idade
def paracadaidade():
    contadormenor = 0
    contadormaior = 0
    for idade in idades:
        if idade >= 18:
            contadormaior += 1
        else:
            contadormenor += 1
    print("Menor de idade ",contadormenor, "Maiores de idade ",contadormaior)


# verificação de idades
def idademedia():
    if 30 <= media:
        print("Base de dados madura.")
    else:
        print("Base de dados jovem.")

#Media das idades
media = sum(idades) / len(idades)
print("A media das idades é ",media)

#Mais velho e mais novo
maisvelho = max(idades)
maisnovo = min(idades)

#chamando função
idademedia()
paracadaidade()