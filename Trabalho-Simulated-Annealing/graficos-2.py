import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import graficos
import pickle

pickle_in = open('results/resultados-sat-2-1/T_matrix-pickle.pickle',"rb")
T = pickle.load(pickle_in)
T = np.array(T)

pickle_in = open('results/resultados-sat-2-1/result_matrix-pickle.pickle',"rb")
res = pickle.load(pickle_in)
res = np.array(res)

pickle_in = open('results/resultados-sat-2-1/alpha_matrix-pickle.pickle',"rb")
alpha = pickle.load(pickle_in)
alpha = np.array(alpha)

pickle_in = open('his-best-sat-2-pickle.pickle',"rb")
his = pickle.load(pickle_in)
his = np.array(his)

k = np.arange(0,      len(his[2])          , 1)



# for i in range(len(res)):
#     for j in range(len(res[i])):
#         if res[i][j] > 493:
#             print('MAX - ',res[i][j])
#             print('T - ', T[i][j])
#             print('Alpha - ', alpha[i][j])
#             print('-----------------------')
#             print()



graficos.print_3d(alpha, 'alpha', T, 'T', res, 'MAX', 'SA', show=True, save=True, path='grafico_sat-2')

#graficos.print_2d(k, 'Epoch', his[2], 'Result', "SA_Best_SAT-2", save=False, show=True)