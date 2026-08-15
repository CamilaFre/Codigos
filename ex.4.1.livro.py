salário = float(input("Digite o seu salário para o cálculo do imposto: "))

base = salário

imposto = 0

if base > 3000:

    imposto = imposto + ((base-3000)*0.35)

    base = 3000

if base > 1000:

    imposto = imposto + ((base-1000)*0.2)

print(f"Salário: R$ {salário:6.2f} Imposto a pagar: R$ {imposto:6.2F}")