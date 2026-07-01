# =========================================================
# 1) IF SIMPLES
# Cenário: Apita se o time entrou na área
# =========================================================
distancia_do_gol = 20

if distancia_do_gol < 18:
    print("Entrou na área. Perigo de gol!")

# =========================================================
# 2) IF / ELSE
# Cenário: o goleiro defendeu ou tomou gol?
# =========================================================
forca_do_chute = 87
reflexo_goleiro = 60

if forca_do_chute < reflexo_goleiro:
    print("Gol!")
else:
    print("Goleiro defendeu!")

# =========================================================
# 3) IF / ELIF / ELSE
# Cenário: que cartão o juiz deu?
# =========================================================
gravidade_da_falta = "grave"  # leve, moderada, grave

if gravidade_da_falta == "leve":
    print("Só advertência")
elif gravidade_da_falta == "moderada":
    print("Cartão amarelo")
else:
    print("Cartão vermelho!")

# =========================================================
# 4) MÚLTIPLOS ELIF
# Cenário: situação do time no jogo
# =========================================================
saldo = 1  # diferença de gols (negativo = perdendo)

if saldo >= 3:
    print("Vitória tranquila")
elif saldo == 2:
    print("Jogo controlado.")
elif saldo == 1:
    print("Vitória apertada")
elif saldo == 0:
    print("Jogo foi empatado")
elif saldo == -1:
    print("Time está perdendo")
else:
    print("Tá uma desgraça! O time tá perdendo feio")


# =========================================================
# 5) IF ANINHADO (com elif dentro) e Operadores Lógicos (AND [&], OR [or] e NOT)
# Cenário: decisão do VAR
# =========================================================
teve_gol = True
revisao_do_var = "mao"  # legal, impedido, mao, falta

if teve_gol:
    print("Gol marcado.")

    if revisao_do_var == "legal":
        print("Gol confirmado.")
    else:
        print("Gol anulado.")
else:
    print("Gol não confirmado.")


if teve_gol and revisao_do_var == "legal":
    print("Gol confirmado")
else:
    print("Gol não confirmado.")

# =========================================================
# 6) IF / ELIF / ELSE COM OPERADORES LÓGICOS E DE COMPARAÇÃO
# Cenário: chance de liderar o grupo
# =========================================================
pontos = 6
saldo_gols = 2
jogo_direto_contra_lider = False
gols_marcados = 7

if pontos >= 7 and saldo_gols > 3:
    print("Já está na liderança")
elif pontos == 6 and jogo_direto_contra_lider and saldo_gols >= 3:
    print("Depende só da vitória")
elif pontos == 6 and (saldo_gols < 3 or gols_marcados < 5):
    print("Precisa ganhar e torcer")
elif pontos < 4 or saldo_gols < -2:
    print("Risco de eliminação")
else:
    print("Classificação indefinida")


# =========================================================
# 7) Condições com texto: o IF também pode ser usado com textos
# =========================================================
nome_jogador = "Cristiano Ronaldo"
if nome_jogador == "Cristiano Ronaldo":
    print("O jogo é cristiano ronaldo")


# =========================================================
# 8) MATCH / CASE
# Cenário: Revisão do Var
# =========================================================
revisao_do_var_novo = "impedido"
match revisao_do_var_novo:
    case "legal":
        print("Gol confirmado")
    case "impedido":
        print("Gol anulado por impedimento")
    case "mao":
        print("Gol anulado por toque de mão")
    case "falta":
        print("Gol anulado por falta")
    case _:
        print("Lance em revisão")

# =========================================================
# 8B) O mesmo exemplo com IF / ELIF / ELSE
# =========================================================
if revisao_do_var == "legal":
    print("Gol confirmado.")
elif revisao_do_var == "impedido":
    print("Gol anulado por impedimento.")
elif revisao_do_var == "mao":
    print("Gol anulado por toque de mão.")
elif revisao_do_var == "falta":
    print("Gol anulado por falta.")
else:
    print("Lance em revisão.")

# =========================================================
# 9) Outros exemplos
# =========================================================
if pontos >= 10:
    print("Classificado")
elif pontos >= 6:
    print("Ainda tem chance")
else:
    print("Eliminado")

posicao = "goleiro"

match posicao:
    case "goleiro":
        print("Defende o gol.")
    case "zagueiro":
        print("Marca os atacantes.")
    case "atacante":
        print("Tenta fazer gols.")
    case _:
        print("Posição não reconhecida.")
