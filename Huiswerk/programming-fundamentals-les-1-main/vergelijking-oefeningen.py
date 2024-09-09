# geef 2 getallen op en kijk of ze gelijk zijn
# 5 en 5 zijn gelijk
a = 5 == 5
print(a)
# 5 en 3 zijn niet gelijk
b = 5 != 5
print(b)

# geef 2 getallen op en kijk of getal1 groter is dan getal2
# 5 is groter dan 3
c = 5 > 3
print(c)
# 3 is niet groter dan 5
c = 5 < 3
print(c)

# geef 2 getallen op en kijk of getal1 kleiner is dan getal2 of gelijk aan getal2
getal1 = 5
getal2 = 3
print(f"{getal1} is kleiner dan {getal2} of gelijk aan {getal2}: ", (getal1 < getal2) or (getal1 == getal2))
# Vergelijking van twee getallen met gebruik van and en or
getal1 = 5
getal2 = 3

print(f"{getal1} is kleiner dan {getal2}" if (getal1 < getal2) else f"{getal1} is niet kleiner dan {getal2}")

getal1 = 3
getal2 = 5

print(f"{getal1} is kleiner dan {getal2}" if (getal1 < getal2) else f"{getal1} is niet kleiner dan {getal2}")

getal1 = 5
getal2 = 5

print(f"{getal1} is kleiner dan {getal2}" if (getal1 < getal2) else f"{getal1} is niet kleiner dan {getal2}")


# Kijk of een string gelijk is aan een andere string
string1 = "John"
string2 = "John"
string3 = "Doeg"
# John is gelijk aan John
print(f"{string1} is gelijk aan {string2}: ", string1 == string2)
# John is niet gelijk aan Doeg
print(f"{string1} is niet gelijk aan {string3}: ", string1 != string3)