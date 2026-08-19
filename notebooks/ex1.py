import sys
import numpy as np
import pandas as pd
import matplotlib
from palmerpenguins import load_penguins
print("Python:", sys.version.split()[0])
print("numpy:", np.__version__)
print("pandas:", pd.__version__)
print("matplotlib:", matplotlib.__version__)
penguins = load_penguins()
print("penguins shape:", penguins.shape)
penguins.head()

'''
INTEGRANTES:
Íris de Campos Melero - 23.01109-2
Guilherme
Lucas Kenzo
Vitor
Yasmin Pacheco Gil Bonilha - 23.01425-3

Saída:

Python: 3.14.0
numpy: 2.5.2
pandas: 3.0.5
matplotlib: 3.10.7
penguins shape: (344, 8)

'''
