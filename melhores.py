import random
import math
import numpy as np
import pickle
from teste import T_vet
from tqdm import tqdm
from time import time

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

        n_its1 = 3000
        n_its2 = 30

        his = []

        self.initial_sol()

        current_cost = self.cont_trues(self.sol)

        for _ in range(1, n_its1):

            for j in range(n_its2):

                new_sol = self.modify_sol_rand(j%2)
                new_cost = self.cont_trues(new_sol)

                delta = new_cost - current_cost

                if(random.random() < math.exp(delta/T)):
                    self.sol = new_sol.copy()
                    current_cost = self.cont_trues(self.sol)
                    his.append(current_cost)

            T = T * alpha
            if T < 0.01:
                #print('break') 
                break

        return his

    def testes(self, T_vet, Alpha_vet):
        
        sair = False
        while True:        
            result = [ T_vet, Alpha_vet, self.SA(T_vet, Alpha_vet) ]
        
            #self.save_data("his-best-sat-1", result)
            
            for i in range(len(result[2])):
                if result[2][i] >= 274:
                    print('MAX - ',result[2][i]),
                    sair = True
            if sair:
                self.save_data("his-best-sat-1", result)
                break
            print('.', end='')

    def save_data(self, save_name, data):
        pickle_out = open(save_name+"-pickle.pickle","wb")
        print('Arquivo gravado como: '+save_name+"-pickle.pickle")
        pickle.dump(data, pickle_out)
        pickle_out.close()
        
    
#T =     [650,  640,  570] 
#MAX =   [275,  275,  274]
#Alpha = [0.96, 0.96, 0.96]

T = 570 
Alpha = 0.96

formu = formula()
formu.read_txt('sat-1.txt')
formu.testes(T , Alpha)
