import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import graficos
import pickle

pickle_in = open('results/resultados-sat-1-1/T_matrix-pickle.pickle',"rb")
T = pickle.load(pickle_in)
T = np.array(T)

pickle_in = open('results/resultados-sat-1-1/result_matrix-pickle.pickle',"rb")
res = pickle.load(pickle_in)
res = np.array(res)

pickle_in = open('results/resultados-sat-1-1/alpha_matrix-pickle.pickle',"rb")
alpha = pickle.load(pickle_in)
alpha = np.array(alpha)

pickle_in = open('his-best-sat-1-pickle.pickle',"rb")
his = pickle.load(pickle_in)
his = np.array(his)

k = np.arange(0,      len(his[2])          , 1)



#graficos.print_3d(alpha, 'alpha', T, 'T', res, 'MAX', 'SA', show=True, save=True, path='grafico_sat-1')

graficos.print_2d(k, 'Epoch', his[2], 'Result', "SA_Best_SAT-1", save=False, show=True)