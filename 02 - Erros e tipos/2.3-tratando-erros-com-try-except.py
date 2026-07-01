# 1) Código que quebra se o usuário digitar errado
gols = int(input("Quantos gols o Brasil fez? "))
print(f"O Brasil fez {gols} gols.")


# 2) ValueError acontecendo
numero = int("três")
print(numero)


# 3) Tratando erro ao digitar os gols do Brasil
try:
    gols = int(input("Quantos gols o Brasil fez? "))
    print(f"O Brasil fez {gols} gols.")

except ValueError:
    print("Você precisa digitar um número inteiro.")


# 4) Analisando os gols do Brasil usando try/except com if
try:
    gols = int(input("Quantos gols o Brasil fez? "))

    if gols >= 3:
        print("O Brasil fez muitos gols!")
    elif gols == 1 or gols == 2:
        print("O Brasil marcou, mas poderia ter feito mais.")
    else:
        print("O Brasil não marcou gols.")

except ValueError:
    print("Você precisa digitar um número inteiro.")


# 5) Pedindo os gols até o usuário digitar um número válido
numero_valido = False

while numero_valido == False:
    try:
        gols = int(input("Quantos gols o Brasil fez? "))

        numero_valido = True

    except ValueError:
        print("Valor inválido. Digite um número inteiro.")

print(f"O Brasil fez {gols} gols.")


# 6) Somando os gols do Brasil em 3 jogos
total_gols = 0

for jogo in range(1, 4):
    numero_valido = False

    while numero_valido == False:
        try:
            gols = int(input(f"Quantos gols o Brasil fez no jogo {jogo}? "))

            numero_valido = True

        except ValueError:
            print("Valor inválido. Digite um número inteiro.")

    total_gols += gols

print(f"Total de gols do Brasil: {total_gols}")


# 7) Mostrando o desempenho do Brasil em cada jogo
total_gols = 0

for jogo in range(1, 4):
    numero_valido = False

    while numero_valido == False:
        try:
            gols = int(input(f"Quantos gols o Brasil fez no jogo {jogo}? "))

            numero_valido = True

        except ValueError:
            print("Valor inválido. Digite um número inteiro.")

    total_gols += gols

    if gols == 0:
        print("O Brasil não marcou nesse jogo.")
    elif gols == 1:
        print("O Brasil marcou 1 gol nesse jogo.")
    else:
        print(f"O Brasil marcou {gols} gols nesse jogo.")

print(f"Total de gols do Brasil: {total_gols}")

media = total_gols / 3

print(f"Média de gols por jogo: {media}")


# =========================================================
# 8) Código Extra da aula para estudos: campanha do Brasil na Copa
# =========================================================

total_gols_brasil = 0
total_gols_adversarios = 0
pontos = 0

for jogo in range(1, 4):
    print(f"Jogo {jogo}")

    numero_valido = False

    while numero_valido == False:
        try:
            gols_brasil = int(input("Quantos gols o Brasil fez? "))

            numero_valido = True

        except ValueError:
            print("Valor inválido. Digite um número inteiro.")

    numero_valido = False

    while numero_valido == False:
        try:
            gols_adversario = int(input("Quantos gols o adversário fez? "))

            numero_valido = True

        except ValueError:
            print("Valor inválido. Digite um número inteiro.")

    total_gols_brasil += gols_brasil
    total_gols_adversarios += gols_adversario

    if gols_brasil > gols_adversario:
        print("Vitória do Brasil!")
        pontos += 3
    elif gols_brasil == gols_adversario:
        print("Empate do Brasil.")
        pontos += 1
    else:
        print("Derrota do Brasil.")

    print("--------------------")

print("Resumo da fase de grupos")
print(f"Total de gols do Brasil: {total_gols_brasil}")
print(f"Total de gols sofridos: {total_gols_adversarios}")
print(f"Pontuação final: {pontos}")

if pontos >= 6:
    print("Brasil classificado para a próxima fase!")
elif pontos >= 4:
    print("Brasil ainda tem chance, mas depende do grupo.")
else:
    print("Brasil em situação difícil na Copa.")
