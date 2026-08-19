import numpy as np

x = np.array([10,20,30,40,50])

print(x.mean(), x.std(), x.sum())

new_x = x - x.mean()
print(new_x.mean())

'''
Saída:
30.0 14.142135623730951 150
0.0
'''