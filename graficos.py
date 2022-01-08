import matplotlib.pyplot as plt


T_inicial = 1
alpha = 0.001
passo_alpha = 0.01
res = []

for T in range(0, 100):
    for alpha in range(0, 100):
        res.append([T, alpha/100, T*((alpha/100)+1)])
        print(T)


for i in range(len(res)):
    print(res[i])
'''plt.plot(xteste, xteste/2)
plt.xlabel('X')
plt.ylabel('Y')
plt.title(r'Linear Regression')
plt.grid(color = 'g', linestyle=':', linewidth=.3)
#plt.savefig('./life_expect_x_years.png', dpi = 300)
plt.show()'''