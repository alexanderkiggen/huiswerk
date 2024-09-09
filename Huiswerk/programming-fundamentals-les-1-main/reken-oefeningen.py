### Laat python 2 getallen optellen en het resultaat printen
#  5 + 3 = 8
x = 5 + 3
print(x)


### Laat python 2 getallen vermenigvuldigen en het resultaat printen
#  3 * 4 = 12
y = 3 * 4
print(y)

### Geef nu het resultaat weer in een string. waar de getallen en het resultaat in staan.
getallen = (f"""
5 + 3 = {x}
3 * 4 = {y}
""")
print(getallen)


### Laat python de wortel van een getal berekenen en het resultaat printen
# De wortel van 16 is 4
getal = 16
wortel = getal ** 0.5
print(wortel)
# Tip gebruik ** om de wortel te berekenen

### Laat python de rest van een deling berekenen en het resultaat printen
#  De rest van 10 / 3 is 1
modulo = 10 % 3
print('Modulo: ', modulo)

### Maak een calculator die 2 getallen optelt, aftrekt, vermenigvuldigd en deelt
# Gebruik hiervoor input om de getallen te vragen
# Voer getal 1 in: 5
# Voer getal 2 in: 3
# 5 + 3 = 8
# 5 - 3 = 2
# 5 * 3 = 15
# 5 / 3 = 1.6666666666666667

getal1 = int(input("Voer getal 1 in: "))
getal2 = int(input("Voer getal 2 in: "))
uitkomst = f"""
{getal1} + {getal2} = {getal1+getal2}
{getal1} - {getal2} = {getal1-getal2}
{getal1} * {getal2} = {getal1*getal2}
{getal1} / {getal2} = {getal1/getal2}
"""
print(uitkomst)

print("hello")