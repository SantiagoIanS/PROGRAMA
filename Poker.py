import random

cartas = [[["Ás ♠", "2 ♠", "3 ♠", "4 ♠", "5 ♠", "6 ♠", "7 ♠", "8 ♠", "9 ♠", "10 ♠", "J ♠", "Q ♠", "K ♠"], ["Ás ♣", "2 ♣", "3 ♣", "4 ♣", "5 ♣", "6 ♣", "7 ♣", "8 ♣", "9 ♣", "10 ♣", "J ♣", "Q ♣", "K ♣"], ["Ás ♥", "2 ♥", "3 ♥", "4 ♥", "5 ♥", "6 ♥", "7 ♥", "8 ♥", "9 ♥", "10 ♥", "J ♥", "Q ♥", "K ♥"], ["Ás ♦", "2 ♦", "3 ♦", "4 ♦", "5 ♦", "6 ♦", "7 ♦", "8 ♦", "9 ♦", "10 ♦", "J ♦", "Q ♦", "K ♦"]]]
cartastodas = ["Ás ♠", "2 ♠", "3 ♠", "4 ♠", "5 ♠", "6 ♠", "7 ♠", "8 ♠", "9 ♠", "10 ♠", "J ♠", "Q ♠", "K ♠", "Ás ♣", "2 ♣", "3 ♣", "4 ♣", "5 ♣", "6 ♣", "7 ♣", "8 ♣", "9 ♣", "10 ♣", "J ♣", "Q ♣", "K ♣", "Ás ♥", "2 ♥", "3 ♥", "4 ♥", "5 ♥", "6 ♥", "7 ♥", "8 ♥", "9 ♥", "10 ♥", "J ♥", "Q ♥", "K ♥", "Ás ♦", "2 ♦", "3 ♦", "4 ♦", "5 ♦", "6 ♦", "7 ♦", "8 ♦", "9 ♦", "10 ♦", "J ♦", "Q ♦", "K ♦"]
maomesa = []
fichasuser = 150
maouser = []
fichasbot = 150
maobot = []
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
segundarodada = []

while len(segundarodada) < 1:
    n = random.choice(cartastodas)
    if n not in segundarodada:
        segundarodada.append(n)
    cartastodas.remove(n)

maomesa.append(segundarodada)

print(f"----SEGUNDA RODADA----")
print(maomesa)
print(*maomesa)

#mões

#testes
print("teste")


