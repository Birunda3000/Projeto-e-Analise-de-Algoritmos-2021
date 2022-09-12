import random
import math
import numpy as np
import pickle
from tqdm import tqdm

class literal:
    def __init__(self, id):
        self.id = abs(id)
        self.signal = 1 if id > 0 else 0

    def return_value(self, sol):
        return self.signal == sol[self.id - 1]

class clause:
    def __init__(self, id, literals):
        self.id = id
        self.literals = literals

    def verify_clause(self, sol):
        return (self.literals[0].return_value(sol) or self.literals[1].return_value(sol)) or self.literals[2].return_value(sol)

class formula:
    def __init__(self):
        self.sol = []
        self.clauses = []
        self.n_literals = 0
        self.n_clauses = 0

    def read_txt(self, name):
        matrix = []
        aux = []
        arq = open(name, 'r')
        for line in arq:
            line = line.strip()
            line = line.split(" ")
            for i in range(len(line)):
                aux.append(int(line[i]))
            matrix.append(aux)
            aux = []
        
        self.n_literals = int(matrix[0][0])
        self.n_clauses = int(matrix[0][1])
        matrix = matrix[1:]

        for i in range(self.n_clauses):
            x1 = literal(matrix[i][0])
            x2 = literal(matrix[i][1])
            x3 = literal(matrix[i][2])
            self.clauses.append(clause(i , [x1,x2,x3]))
  
    def initial_sol(self):
        for _ in range(self.n_literals):
            self.sol.append(random.randint(0,1))

    def modify_sol_rand(self, half):
        mod_sol = self.sol.copy()
        if half == 0:
            m = random.randint(0, self.n_literals/2)
            mod_sol[m] = (mod_sol[m] + 1) % 2
        else:
            m = random.randint(self.n_literals/2, self.n_literals - 1)
            mod_sol[m] = (mod_sol[m] + 1) % 2

        return mod_sol

    def cont_trues(self, sol):
        t = 0
        for clause in self.clauses:
            if clause.verify_clause(sol):
                t += 1
        return t
    
    def SA(self, T, alpha):

        n_its1 = 1000
        n_its2 = 100

        self.initial_sol()

        current_cost = self.cont_trues(self.sol)

        for _ in range(1, n_its1):

            for j in range(n_its2):

                new_sol = self.modify_sol_rand(j%2)
                new_cost = self.cont_trues(new_sol)

                delta = new_cost - current_cost

                aux = delta/T
                
                if aux > 700: aux = 700
                if aux < -700: aux = -700

                if(random.random() < math.exp(aux)):
                    self.sol = new_sol.copy()
                    current_cost = self.cont_trues(self.sol)


            T = T * alpha
            if T < 0.0001: break

        return self.cont_trues(self.sol)

    def testes(self):

        T_vet = []
        alpha_vet = []
        result_vet = []

        for T in tqdm(range(100, 1000, 100)):

            T_aux = []
            alpha_aux = []
            result_aux = []

            for alpha in tqdm(np.arange(0.1, 0.9, 0.1)):

                max_result = 0

                for _ in range(3):
                    result = self.SA(T, alpha)
                    if result > max_result : max_result = result
                
                T_aux.append(T)
                alpha_aux.append(alpha)
                result_aux.append(max_result)

            T_vet.append(T_aux)
            alpha_vet.append(alpha_aux)
            result_vet.append(result_aux)

        
        self.save_data("T_matrix3", T_vet)
        self.save_data("alpha_matrix3", alpha_vet)
        self.save_data("result_matrix3", result_vet)


    def save_data(self, save_name, data):
        pickle_out = open(save_name+".pickle","wb")
        print('Arquivo gravado como: '+save_name+".pickle")
        pickle.dump(data, pickle_out)
        pickle_out.close()
        
    

        




formu = formula()
formu.read_txt('sat-3.txt')
formu.testes()















"""
TESTES QUE DERAM O RESULTADO:

272/275:
 n_iterations1 = 40
        n_iterations2 = 1000
        T = 1000
        alpha = 0.09

Chegou no 499:

n_iterations1 = 15
n_iterations2 = 400
T = 600
alpha = 0.35

Valores q mais deram certo pro sat-3:

n_iterations1 = 20
n_iterations2 = 500
T = 700
alpha = 0.4

if T < 0.005: break


"""