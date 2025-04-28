sabores = ["Calabresa", "Sorvete", "Lombo", "Chocolate", "Portuguesa"]
borda = ["Sem borda", "Chocolate", "Catupiry", "Cheddar"]
tamanho = ["Grandita", "Pequenita", "Medita"]
localidade = ["Planaltina", "Sobradinho", "Mestre d'Armás"]
escolhas = []
metade = ["Um sabor", "Dois sabores"]

valor_sabores = [27, 40, 35, 40, 30]
valor_borda = [0, 5, 5, 5]
valor_tam = [10, 5, 8]
frete = [0, 10, 7]
valor_metade = [0, 8]

print("BEM VINDOS A LÓGICA DO SABOR")
print(' ')

for i in range(len(metade)):
    print(f"{i + 1}. {metade[i]}: Acrécimo de R${valor_metade[i]}")
    print(' ')
escolhas.append(int(input("Você gostaria de 1 ou 2 sabores de pizza? ")) - 1)

if escolhas[0] == 1:
    print(' ')
    for i in range(len(sabores)):
        print(f"{i + 1}. {sabores[i]}: R$ {valor_sabores[i]}")
        print(' ')
    escolhas.append(int(input("Escolha o primeiro sabor de pizza: ")) - 1)
    print(' ')
    escolhas.append(int(input("Escolha o segundo sabor de pizza: ")) - 1)
else:
    for i in range(len(sabores)):
        print(f"{i + 1}. {sabores[i]}: R$ {valor_sabores[i]}")
        print(' ')
    escolhas.append(int(input("Escolha seu sabor de pizza: ")) - 1)

for i in range(len(borda)):
    print(f"{i + 1}. {borda[i]}: R$ {valor_borda[i]}")
    print(' ')
escolhas.append(int(input("Escolha a borda da pizza: ")) - 1)
print(" ")

for i in range(len(tamanho)):
    print(f"{i + 1}. {tamanho[i]}: R$ {valor_tam[i]}")
    print(' ')
escolhas.append(int(input("Escolha o tamanho da pizza: ")) - 1)
print(" ")

for i in range(len(localidade)):
    print(f"{i + 1}. {localidade[i]}: R$ {frete[i]}")
    print(' ')
escolhas.append(int(input("Escolha a localidade: ")) - 1)
print(" ")

total = 0

if escolhas[0] == 1:
    total = valor_sabores[escolhas[1]] + valor_sabores[escolhas[2]] + valor_metade[1] + valor_borda[escolhas[3]] + valor_tam[escolhas[4]] + frete[escolhas[5]]
else:
    total = valor_sabores[escolhas[1]] + valor_borda[escolhas[2]] + valor_tam[escolhas[3]] + frete[escolhas[4]]

print(f"O total da sua compra é de: R$ {total:.2f}")
confirmação = input("Deseja confirmar e finalizar a sua compra? (s/n) ")
escolhas.append(confirmação)

if escolhas[-1].lower() == "s":
    print("Muito Obrigada pela preferência.")
elif escolhas[-1].lower() == "n":
    print("Vai confirmar simmm")