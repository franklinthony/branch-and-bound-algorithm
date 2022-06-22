def Leitura(fileName):
    # Abrindo o arquivo para leitura
    with open(fileName) as file:
        lista = [list(map(int, row.split())) for row in file]
            
    # Passando o número de variáveis para 'num_var'
    num_var = lista[0][0]
    # Passando o número de restrições para 'num_res'
    num_res = lista[0][1]
    lista.pop(0)

    # Coeficientes da função objetivo
    coef = lista[0]
    lista.pop(0)

    # Restrições
    rest = lista

    return(num_var, num_res, coef, rest)
