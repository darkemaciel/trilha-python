# ----------------------------------------------------------
# VARIÁVEIS E ATRIBUIÇÃO
# ----------------------------------------------------------
# O símbolo = significa ATRIBUIÇÃO, não igualdade
# nome_da_variavel = valor / conteúdo

nome = "Darke"  # str  — texto sempre entre aspas (duplas ou simples)
idade = 33  # int  — número inteiro
estado = "Espírito Santo"  # # str  — texto sempre entre aspas (duplas ou simples)
tem_cachorro = True  # bool — True ou False (com maiúscula)
altura = 1.72  # float — número com ponto flutuante

print(nome)
print(idade)
print(estado)
print(tem_cachorro)
print(altura)

# ----------------------------------------------------------
# TIPOS PRIMITIVOS
# ----------------------------------------------------------
# Você pode descobrir o tipo de qualquer variável com type()
print(type(nome))  # <class 'str'>
print(type(idade))  # <class 'int'>
print(type(estado))  # <class 'str'>
print(type(tem_cachorro))  # <class 'bool'>
print(type(altura))  # <class 'float'>

# ----------------------------------------------------------
# REATRIBUIÇÃO
# ----------------------------------------------------------
# Variáveis podem ter seu valor trocado a qualquer momento
# A etiqueta agora aponta para outro valor (para outro objeto na memória que contêm o novo alor)

idade = 30
print(idade)  # 30

idade = 50
print(idade)  # 50

idade = "Darke Maciel"  # "Luiza Vieira"
print(idade)

# ----------------------------------------------------------
# REGRAS DE NOMENCLATURA
# ----------------------------------------------------------
# nome_da_variavel = valor / conteúdo

maça = 144  # não faça isso!
# Sempre coloque nomes facéis de identificar do que essa variável se trata / conteúdo que ela guarda!

# REGRAS NA CRIAÇÃO DAS VARIÁVEIS
# VÁLIDO
minha_altura = 1.58  # snake_case — padrão Python
minhaAltura = 1.58  # CamelCase
nome1 = "Luiza"  # número no meio ou no final: ok
_privado = "interno"  # underline no início: válido

# INVÁLIDO — descomente para ver o erro
# 1nome = "erro"          # não pode começar com número
# meu nome = "erro"       # não pode ter espaço
# minha-altura = 1.58     # hífen não é válido em variáveis
# Utilizar caracteres especiais: @,!,?,$ (EXECETO _ (underline))
# PALAVRAS CHAVES que NÃO PODE ser NOMES de VARIÁVEIS
# if, class, for, False, None, and, True, print, import, return, try, as, await, break, or, not, as

# Case-sensitive: Idade e idade são variáveis DIFERENTES
Cachorro = "Snoppy"
cachorro = "Bobby"
print(Cachorro)  # "Snoppy"
print(cachorro)  # "Bobby"


# ----------------------------------------------------------
# 5. COMENTÁRIOS E SINTAXE BÁSICA
# ----------------------------------------------------------

# Tudo após # é um comentário — Python ignora
# Comentários servem para ajudar na legibilidade, documentação, manutenção...
# Em Python, você pode usar aspas triplas (''' ... ''' ou """ ... """) para escrever blocos de texto em várias linhas. Muitas pessoas usam isso como se fosse um “comentário longo”/
"""
Esse bloco é, na verdade, uma string multilinha.

Se não for atribuída a nenhuma variável, o Python simplesmente a ignora.
Ainda assim, ela é interpretada como uma string.
"""

# Python executa linha por linha, de cima pra baixo (leitura sequencial)
# A ordem importa: não dá pra usar uma variável antes de criá-la  # agora funciona

# print(), type(), entre outras funções, elas são Built-in do Python
# "Built-in" em Python refere-se a funções, tipos de dados e exceções que já vêm integrados no núcleo da linguagem

"""
FECHAMENTO DO BLOCO

Então, resumindo o que a gente viu até aqui:
 - Uma variável é um identificador (ou rótulo) que referencia um objeto armazenado na memória, o qual contém o valor que queremos utilizar no programa.
 - O = em Python é atribuição, não igualdade
 - Existem quatro tipos primitivos principais: str (string), int (integer), float e bool (booleano)
 - Variáveis podem ser reatribuídas
 - A gente pode usar print() para ver o valor e type() para ver o tipo
"""
