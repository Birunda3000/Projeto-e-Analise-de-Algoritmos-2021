import classes

formu = classes.formula()
formu.ler_arquivo('sat-0.txt')
formu.atribuir_valores()
formu.exibir_formula()
formu.exibir_valores()
v, f = formu.conta_verdade()
print('Verdade - ', v, ' | Falso - ', f)