import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import graficos
import pickle

aux = open("./alpha_matrix1.pickle","rb")
alpha2 = np.array(pickle.load(aux))
aux.close()
aux = open("./T_matrix1.pickle","rb")
T2 = np.array(pickle.load(aux))
aux.close()
aux = open("./result_matrix1.pickle","rb")
MAX2 = np.array(pickle.load(aux))
aux.close()

print(alpha2)
print(T2)
print(MAX2)

#alpha2, T2 = np.meshgrid(range(10), range(10))
#MAX2 = (alpha2**3 + T2**2 - 30) / 2 

#graficos.print_2d(alpha2, 'alpha', MAX2, 'Max', 'SA', show=True, save=False)

graficos.print_3d(alpha2, 'alpha', T2, 'T', MAX2, 'MAX', 'SA', show=True, save=False)

