# Solicitar peso e altura ao usuário
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

# Calcular o IMC
imc = peso / (altura ** 2)

# Exibir o resultado
print(f"Seu IMC é: {imc:.2f}")

# Classificar o IMC
if imc < 18.5:
    print("Classificação: Abaixo do peso")
elif 18.5 <= imc < 24.9:
    print("Classificação: Peso normal")
elif 25 <= imc < 29.9:
    print("Classificação: Sobrepeso")
else:
    print("Classificação: Obesidade")
