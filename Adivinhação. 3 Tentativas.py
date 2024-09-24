adivinha = 5
tentativas = 0
limite_tentativas = 3

while tentativas < limite_tentativas:
    numero = int(input("Adivinhe qual é o número correto: "))
    if numero == adivinha:
        print("Parabéns! Você adivinhou o número!")
        break
    else:
        tentativas += 1
        print(f"Senha incorreta, você tem {limite_tentativas - tentativas} chance(s).")
if tentativas == limite_tentativas:
    print("Você excedeu o limite de tentativas. Não foi dessa vez")