import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import graficos


alpha = np.arange(0.001, 0.999, 0.01)
MAX =  (alpha*10)**2

alpha2, T2 = np.meshgrid(range(3), np.arange(0.001, 0.300, 0.01))

#print(alpha2)

#print(T2)

T_vet = []
T_aux = []
alpha_vet = []
alpha_aux = []
res_vet = []
res_aux = []

for T in range(1000):
    T_aux = []
    alpha_aux = []
    res_aux = []

    for alpha in range(100):
        #executar SA
        T_aux.append(T)
        alpha_aux.append(alpha)
        res_aux = []

    T_vet.append(T_aux)
    alpha_vet.append(alpha_aux)
    res_vet.append(res_aux)

    
