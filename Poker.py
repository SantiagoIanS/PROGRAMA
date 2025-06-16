import random


cartas = [[["Ás ♠", "2 ♠", "3 ♠", "4 ♠", "5 ♠", "6 ♠", "7 ♠", "8 ♠", "9 ♠", "10 ♠", "J ♠", "Q ♠", "K ♠"], ["Ás ♣", "2 ♣", "3 ♣", "4 ♣", "5 ♣", "6 ♣", "7 ♣", "8 ♣", "9 ♣", "10 ♣", "J ♣", "Q ♣", "K ♣"], ["Ás ♥", "2 ♥", "3 ♥", "4 ♥", "5 ♥", "6 ♥", "7 ♥", "8 ♥", "9 ♥", "10 ♥", "J ♥", "Q ♥", "K ♥"], ["Ás ♦", "2 ♦", "3 ♦", "4 ♦", "5 ♦", "6 ♦", "7 ♦", "8 ♦", "9 ♦", "10 ♦", "J ♦", "Q ♦", "K ♦"]]]
cartastodas = ["Ás ♠", "2 ♠", "3 ♠", "4 ♠", "5 ♠", "6 ♠", "7 ♠", "8 ♠", "9 ♠", "10 ♠", "J ♠", "Q ♠", "K ♠", "Ás ♣", "2 ♣", "3 ♣", "4 ♣", "5 ♣", "6 ♣", "7 ♣", "8 ♣", "9 ♣", "10 ♣", "J ♣", "Q ♣", "K ♣", "Ás ♥", "2 ♥", "3 ♥", "4 ♥", "5 ♥", "6 ♥", "7 ♥", "8 ♥", "9 ♥", "10 ♥", "J ♥", "Q ♥", "K ♥", "Ás ♦", "2 ♦", "3 ♦", "4 ♦", "5 ♦", "6 ♦", "7 ♦", "8 ♦", "9 ♦", "10 ♦", "J ♦", "Q ♦", "K ♦"]
maomesa = []
fichasuser = 150
maouser = []
fichasbot = 150
maobot = []
valores_cartas = {"Ás ♠": 14, "2 ♠": 2, "3 ♠": 3, "4 ♠": 4, "5 ♠": 5, "6 ♠": 6, "7 ♠": 7, "8 ♠": 8, "9 ♠": 9, "10 ♠": 10, "J ♠": 11, "Q ♠": 12, "K ♠": 13, "Ás ♣": 14, "2 ♣": 2, "3 ♣": 3, "4 ♣": 4, "5 ♣": 5, "6 ♣": 6, "7 ♣": 7, "8 ♣": 8, "9 ♣": 9, "10 ♣": 10, "J ♣": 11, "Q ♣": 12, "K ♣": 13, "Ás ♥": 14, "2 ♥": 2, "3 ♥": 3, "4 ♥": 4, "5 ♥": 5, "6 ♥": 6, "7 ♥": 7, "8 ♥": 8, "9 ♥": 9, "10 ♥": 10, "J ♥": 11, "Q ♥": 12, "K ♥": 13, "Ás ♦": 14, "2 ♦": 2, "3 ♦": 3, "4 ♦": 4, "5 ♦": 5, "6 ♦": 6, "7 ♦": 7, "8 ♦": 8, "9 ♦": 9, "10 ♦": 10, "J ♦": 11, "Q ♦": 12, "K ♦": 13}
espadas = cartas[0][0]
paus = cartas[0][1]
copas = cartas[0][2]
ouros = cartas[0][3]

while len(maomesa) < 3:
    n = random.choice(cartastodas)
    if n not in maomesa:
        maomesa.append(n)
    cartastodas.remove(n)

while len(maouser) < 2:
    n =random.choice(cartastodas)
    if n not in maouser:
        maouser.append(n)
    cartastodas.remove(n)

#Por enquanto n vai ter bot
#while len(maobot) < 5:
#    n =random.choice(cartas)
#    if n not in maobot:
#        maobot.append(n)
#    cartas.remove(n)

print(f"----PRIMEIRAS RODADA----")
print("(", end="")
print(", ".join(maomesa), end="")
print(")")
print(" ")
print(f"Sua mão: ", end="")
print(", ".join(maouser))
print(f"Seu total de fichas são: {fichasuser}")

aposta1 = int(input("Quantas fichas você apostará na primeira rodada? "))
fichasuser = fichasuser - aposta1

print(f"Seu total de fichas atuais são: {fichasuser}")
print(f"Fichas na mesa: {aposta1}")
segundarodada = ""

n = random.choice(cartastodas)
if n not in segundarodada:
    segundarodada = n
cartastodas.remove(n)

maomesa.append(segundarodada)
print("")
print(f"----SEGUNDA RODADA----")
print(maomesa)
print(" ")
print(f"Sua mão: ", end="")
print(", ".join(maouser))
print(f"Seu total de fichas são: {fichasuser}")

aposta2 = int(input("Quantas fichas você apostará na segunda rodada? "))
fichasuser = fichasuser - aposta2
aposta = aposta1 + aposta2

print(f"Seu total de fichas atuais são: {fichasuser}")
print(f"Fichas na mesa: {aposta}")
print("")

terceirarodada = ""

n = random.choice(cartastodas)
if n not in terceirarodada:
    terceirarodada = n
cartastodas.remove(n)

maomesa.append(terceirarodada)
print(f"----TERCEIRA RODADA----")
print(maomesa)
print(" ")
print(f"Sua mão: ", end="")
print(", ".join(maouser))
print(f"Seu total de fichas são: {fichasuser}")

aposta3 = int(input("Quantas fichas você apostará na segunda rodada? "))
fichasuser = fichasuser - aposta3
aposta = aposta1 + aposta2 + aposta3

print(f"Seu total de fichas atuais são: {fichasuser}")
print(f"Fichas na mesa: {aposta}")
maopoker = []
maopoker = maopoker + maomesa
maopoker = maopoker + maouser
maopoker.sort()
print(f", ".join(maopoker))

def valor_carta(cartastodas):
    partes = cartastodas.strip().split()  # exemplo: "10 ♠" vira ["10", "♠"]
    if len(partes) >= 1:
        valor = partes[0]
        return valores_cartas.get(valor, 0)  # retorna 0 se não encontrar (segurança)
    return 0

def Straight(mao):
    valores = [valor_carta(c) for c in mao]
    valores = list(set(valores))
    if 14 in valores:
        valores.append(1)
    valores.sort()
    for i in range(len(valores) - 4):
        if valores[i] + 1 == valores[i+1] and \
            valores[i] + 2 == valores[i+2] and \
            valores[i] + 3 == valores[i+3] and \
            valores[i] + 4 == valores[i+4]:
            return True
    return False

#mões
#Royal Straight Flush



#Straight Flush

#Quadra

#Full House

#Flush

#Straight

if Straight(maopoker):
    print("Você tem uma sequência (Straight)!")
else:
    print("Você NÃO tem uma sequência.")

#Trinca

#Dois pares

#Par

#Carta alta