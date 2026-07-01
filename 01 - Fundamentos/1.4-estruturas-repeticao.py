# =========================================================
# 1) CÓDIGO REPETITIVO SEM LOOP
# =========================================================
print("Cobrança de pênalti 1: o jogador ajeita a bola...")
print("Cobrança de pênalti 2: o jogador ajeita a bola...")
print("Cobrança de pênalti 3: o jogador ajeita a bola...")
print("Cobrança de pênalti 4: o jogador ajeita a bola...")
print("Cobrança de pênalti 5: o jogador ajeita a bola...")


# =========================================================
# 2) FOR COM STRING
# Cenário: percorrendo o grito da torcida letra por letra
# =========================================================
grito = "GOL"

for letra in grito:
    print(letra)

print("A toricda terminou de grita!")


# =========================================================
# 3) FOR COM RANGE
# Cenário: repetindo cobranças de pênalti automaticamente
# =========================================================
for cobranca in range(1, 6):
    print(f"Cobrança {cobranca}: o jogador ajeita a bola...")


# =========================================================
# 4) FOR COM RANGE
# =========================================================
for numero in range(1, 11):
    print(numero)


# =========================================================
# 5) FOR COM IF DENTRO
# Cenário: rodadas da Copa do Mundo
# =========================================================
for rodada in range(1, 6):
    print(f"Rodada {rodada} da copa do mundo")

    if rodada == 5:
        print("Última rodada! Jogo decisivo!")


# =========================================================
# 6) FOR COM INPUT, IF/ELSE E CONTADOR
# Cenário: contar quantos gols o Brasil fez em lances perigosos
# =========================================================
gols_brasil = 0

for lance in range(1, 4):
    print(f"Lance perigoso, número {lance}")

    resultado = input("Foi gol do Brasil? Digite sim ou nao: ")

    if resultado == "sim":
        gols_brasil += 1
        print("GOOOOOOOL!")
    else:
        print("Não foi gol...")

print("Fim de jogo!")
print(f"Total de gols do Brasil: {gols_brasil}")


# =========================================================
# 7) WHILE COM CONTADOR
# Cenário: repetir cobranças enquanto o número for menor ou igual a 5
# =========================================================
cobranca = 1

while cobranca <= 5:
    print(f"Cobrança {cobranca}: o jogador ajeita a bola...")
    cobranca += 1


# =========================================================
# 8) WHILE COM INPUT
# Cenário: continuar tentando até acertar o pênalti
# =========================================================
resultado = input("Acertou o pênalti? Digite sim ou não: ")

while resultado != "sim":
    print("Errou... tente de novo!")
    resultado = input("Acertou o pênalti agora? Digite sim ou não: ")

print("Boa! O jogador acertou o pênalti")


# =========================================================
# 9) WHILE + FOR + IF
# Cenário: treino continua até o time alcançar 3 gols
# =========================================================
gols = 0
rodada = 1

while gols < 3:
    print(f"\nRodada de treino {rodada}")

    for cobranca in range(1, 4):
        print(f"Cobrança {cobranca}")

        resultado = input("Foi gol? Digite sim ou nao: ")

        if resultado == "sim":
            gols += 1
            print("GOOOOOL!")
        else:
            print("Errou...")

    print(f"Total de gols até agora: {gols}")
    rodada += 1

print("\nTreino finalizado!")
print("O time alcançou a meta de 3 gols.")
