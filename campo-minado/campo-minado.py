
# campo minado

# criar o tabuleiro
tabuleiro = []
for i in range(10):
    linha = []
    for j in range(10):
        linha.append("?")
    tabuleiro.append(linha)
# rastrear bombas
bombas = set()
jogadas = set()
# criar as bombas
import random
for i in range(10):
    linha = random.randint(0, 9)
    coluna = random.randint(0, 9)
    bombas.add(f"{linha}{coluna}")
    # tabuleiro[linha][coluna] = "*"
# criar a jogada
# 1. solicitar a jogada

# verificar se a jogada é válida
def verificar_jogada_valida(linha, coluna):
    if linha < 0 or linha > 9:
        return False
    if coluna < 0 or coluna > 9:
        return False
    if f"{linha}{coluna}" in jogadas:
        return False
    return True
# verificar se a jogada é bomba
def verificar_jogada_bomba(linha, coluna):
    if f"{linha}{coluna}" in bombas:
        return True
    return False

# verificar se a jogada é vitoriosa
def verificar_vitoria():
    if len(jogadas) == 90:
        return True
    return False

# mostrar o tabuleiro
def mostrar_tabuleiro():
    for linha in tabuleiro:
        for coluna in linha:
            print(coluna, end=" ")
        print()
    print()    
mostrar_tabuleiro()
print(bombas)

# mostrar o tabuleiro com as bombas
def mostrar_tabuleiro_bombas():
    for linha in range(10):
        for coluna in range(10):
            if f"{linha}{coluna}" in bombas:
                print("*", end=" ")
            else:
                print(tabuleiro[linha][coluna], end=" ")
        print()
    print()    
# mostrar_tabuleiro_bombas()


# 2. verificar se a jogada é válida
# 3. verificar se a jogada é bomba
# 4. verificar se a jogada é vitoriosa
# 5. mostrar o tabuleiro
# 5. verificar se a jogada é válida