powers = []
for a in range(2, 101):
    for b in range(2, 101):
        powers.append(a**b)
#Suppresion de tous les doublons de la liste powers
resultat = len(list(set(powers)))
print(resultat)