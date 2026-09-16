nome = input("Digite seu nome: ")
email = input ("Digite seu e-mail: ")
pos = email.find("@")
#print(pos)
#print(email[pos:])

if nome == '' or email == '':
    print("Digite seu nome e/ou e-mail corretamente.")
elif "@" in email and "." in email[pos:]:
    print(email)
else:
    print("E-mail inválido")