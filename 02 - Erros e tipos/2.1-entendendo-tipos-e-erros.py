# =========================================================
# 1) TYPEERROR
# Cenário: tentando somar texto com número
# =========================================================

gols_brasil = "3"
gol_extra = 1

# Esse código gera TypeError, porque tenta somar str com int.
# Descomente para testar:

# total_gols = gols_brasil + gol_extra
# print(total_gols)

# =========================================================
# 2) CORRIGINDO O ERRO
# =========================================================
gols_brasil = 3
gol_extra = 1

total_gols = gols_brasil + gol_extra

print(total_gols)


# =========================================================
# 3) RELEMBRANDO TIPOS PRIMITIVOS
# =========================================================

nome_time = "Brasil"
gols = 3
media_gols = 2.5
classificado = True

print(nome_time)
print(gols)
print(media_gols)
print(classificado)


# =========================================================
# 4) TYPE CHECK COM TYPE()
# =========================================================

nome_time = "Brasil"
gols = 3
media_gols = 2.5
classificado = True

print(type(nome_time))
print(type(gols))
print(type(media_gols))
print(type(classificado))


# =========================================================
# 5) INVESTIGANDO O TYPEERROR
# =========================================================
gols_brasil = "3"
gol_extra = 1

print(type(gols_brasil))
print(type(gol_extra))


# =========================================================
# 6) TYPE CHECK COM ISINSTANCE()
# Cenário: verificando se uma variável é int
# =========================================================

# O isinstance() pergunta se um valor é de um tipo específico.
# A resposta dessa verificação é True ou False.

gols = 3

if isinstance(gols, int):
    print("A variável gols é um número inteiro.")
else:
    print("A variável gols não é um número inteiro.")


# =========================================================
# 7) ISINSTANCE COM TEXTO
# =========================================================
gols = "3"

if isinstance(gols, int):
    print("Posso fazer contas com esse valor.")
else:
    print("Esse valor não é um número inteiro.")


# =========================================================
# 8) DIFERENÇA ENTRE TYPE() E ISINSTANCE()
# =========================================================
gols = 3

print(type(gols))
print(isinstance(gols, int))


# =========================================================
# 9) TYPE HINT
# =========================================================

# Type Hint é uma dica de tipo.
# Ele ajuda a deixar claro qual tipo de valor esperamos usar.

nome_time: str = "Brasil"
gols: int = 3
media_gols: float = 2.5
classificado: bool = True

print(nome_time)
print(gols)
print(media_gols)
print(classificado)


# =========================================================
# 10) TYPE HINT NÃO FORÇA O TIPO
# =========================================================

# Mesmo indicando que gols deveria ser int,
# o Python ainda permite trocar o valor para uma string.
# Isso não é uma boa prática, mas mostra que Type Hint é dica, não trava.

gols: int = 3

gols = "três"

print(gols)
print(type(gols))


# =========================================================
# 11) COMPARANDO SEM TYPE HINT E COM TYPE HINT
# =========================================================

# Sem Type Hint
time = "Brasil"
gols = 3
classificado = True

print(time)
print(gols)
print(classificado)


# Com Type Hint
time: str = "Brasil"
gols: int = 3
classificado: bool = True

print(time)
print(gols)
print(classificado)


# =========================================================
# 12) EXEMPLO FINAL
# =========================================================

time: str = "Brasil"
adversario: str = "Argentina"
gols: int = 3
classificado: bool = True

print(f"{time} fez {gols} gols contra {adversario}.")

print(type(time))
print(type(adversario))
print(type(gols))
print(type(classificado))

if isinstance(gols, int):
    print("A variável gols pode ser usada em cálculos.")
else:
    print("A variável gols não é um número inteiro.")

if classificado:
    print("O time está classificado.")
else:
    print("O time não está classificado.")
