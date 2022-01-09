import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import graficos

alpha = np.arange(0.001, 0.999, 0.01)
MAX =  (alpha*10)**2

alpha2, T2 = np.meshgrid(range(10), range(10))
MAX2 = (alpha2**3 + T2**2 - 30) / 2 

graficos.print_2d(alpha, 'alpha', MAX, 'Max', 'SA', show=True, save=False)

graficos.print_3d(alpha2, 'alpha', T2, 'T', MAX2, 'MAX', 'SA', show=True, save=False)

print('Alpha', alpha2)
print()
print('T', T2)
print()
print('MAX', MAX2)