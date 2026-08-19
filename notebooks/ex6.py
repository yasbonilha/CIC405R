from palmerpenguins import load_penguins

penguins = load_penguins()

print(penguins.species.value_counts())

print(penguins.island.value_counts())

'''
Saída:

species
Adelie       152
Gentoo       124
Chinstrap     68
Name: count, dtype: int64

island
Biscoe       168
Dream        124
Torgersen     52
Name: count, dtype: int64

As contagens são as mesmas. Entretanto, o pandas ordena por ordem de frequência, enquanto o R ordena por ordem alfabética.
'''