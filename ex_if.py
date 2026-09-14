categoria = input("Digite a categoria do produto: ")
produto = input("Digite o produto: ")
estoque = input("Digite a qtde de em estoque: ")

if categoria == '' or produto == '' or estoque == '' :

    print("Estão faltando informações")

elif categoria == "alimentos":
    if int(estoque) < 50:
        print(f"Solicitar {produto} à equipe de compras, temos apenas {estoque} em estoque")
elif categoria == "bebidas":
    if int(estoque) < 75:
        print(f"Solicitar {produto} à equipe de compras, temos apenas {estoque} em estoque")
elif categoria == "limpeza":
    if int(estoque) < 30:
        print(f"Solicitar {produto} à equipe de compras, temos apenas {estoque} em estoque")