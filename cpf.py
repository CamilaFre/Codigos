cpf = input("Digite o CPF:" )
cpf = cpf.strip()
cpf = cpf.replace('.','')
cpf = cpf.replace('-', '')


if not cpf.isnumeric() or len(cpf) < 11:
    print("Digite corretamente")

else:
    print(cpf)