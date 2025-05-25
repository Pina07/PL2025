import sys

def extrair_numeros(token):
    nums = []
    atual = ""
    for ch in token:
        if ch.isdigit():
            atual += ch
        else:
            if atual:
                nums.append(int(atual))
                atual = ""
    if atual:
        nums.append(int(atual))
    return nums



soma_ligada = True
soma_total = 0
ultimo_foi_igual = False

for linha in sys.stdin:
    tokens = linha.split()
    eco = []
    
    for token in tokens:
        if token.lower() == "on":
            soma_ligada = True
            eco.append(token)
            continue
        elif token.lower() == "off":
            soma_ligada = False
            eco.append(token)
            continue

        if "=" in token:
            partes = token.split("=")
            reconstruido = ""
            for i, parte in enumerate(partes):
                if soma_ligada:
                    nums = extrair_numeros(parte)
                    if nums:
                        soma_total += sum(nums)
                reconstruido += parte
                if i < len(partes) - 1:
                    reconstruido += "="
                    eco.append(reconstruido)
                    print(" ".join(eco))
                    print(">>", soma_total)
                    eco = []
                    reconstruido = ""
                    ultimo_foi_igual = True
            if reconstruido:
                if reconstruido.lower() == "on":
                    soma_ligada = True
                elif reconstruido.lower() == "off":
                    soma_ligada = False
                eco.append(reconstruido)
                ultimo_foi_igual = False
        else:
            if soma_ligada:
                nums = extrair_numeros(token)
                if nums:
                    soma_total += sum(nums)
            eco.append(token)
            ultimo_foi_igual = False
    if eco:
        print(" ".join(eco))
        if "=" in " ".join(eco):
            print(">>", soma_total)
            ultimo_foi_igual = True

# Garante que imprime no fim, se não foi impresso na última linha
if not ultimo_foi_igual:
    print(">>", soma_total)