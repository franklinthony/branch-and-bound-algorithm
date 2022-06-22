from Modelo import Modelo
from Leitura import Leitura
from Resolver import Resolver
from copy import copy
from copy import deepcopy

# FUNÇÃO QUE RETORNA O INDICE DO NÚMERO 'K' MAIS PROXIMO DADA UMA LISTA 'lst'
def closest(lst, K):       
    return lst.index(lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))])
# VARIÁVEL GLOBAL DA PILHA  
pilha = []
# FUNÇÃO QUE FAZ A RAMIFICAÇÃO DE UM NÓ E ADICIONA OS NOVOS NÓS NA PILHA
def Ramificar(modelo,indice):
    #RAMIFICAR ABAIXO
    modelo_2 = deepcopy(modelo)
    lista_2 = Modelo.getRest_0(modelo_2)
    lista_2[indice] = 1
    Modelo.setRest_0(modelo_2,lista_2)
    pilha.insert(len(pilha),modelo_2)
    #RAMIFICAR ACIMA
    modelo_1 = deepcopy(modelo)
    lista_1 = Modelo.getRest_1(modelo_1)
    lista_1[indice] = 1
    Modelo.setRest_1(modelo_1,lista_1)
    pilha.insert(len(pilha),modelo_1)
########################################  
############# MAIN #####################
########################################
# VARIÁVEL GLOBAL DA MELHOR SOLUÇÃO ÓTIMA ATUAL
Z_global = 0
# ARRAY REFERENTE AO VALOR DAS VARIÁVEIS 'X' CORRESPONDENTE À MELHOR SOLUÇÃO ATUAL
val_var_global = 0

# REALIZA A LEITURA DA INSTACIA
retorno = Leitura('instance-1.txt')

# ARRAYS CORRESPONDENTES AS RESTRIÇÕES DE 0 E 1 QUE SERÃO ADICIONADAS NA RAMIFICAÇÃO 
restricoes_zero = []
restricoes_um = []
for i in range(retorno[0]):
    restricoes_zero.append(0)
    restricoes_um.append(0)

# CRIAÇÃO DO NÓ(MODELO) RAIZ
modelo_raiz = Modelo(retorno[0],retorno[1],retorno[2],retorno[3],restricoes_zero,restricoes_um,None,None)

# RESOLVENDO O NÓ RAIZ
resolucao_raiz = Resolver(modelo_raiz)
# ATUALIZA O MODELO COM O RESULTADO ENCONTRADO
modelo_raiz.vals_vars = resolucao_raiz[0]
modelo_raiz.z = resolucao_raiz[1]

#VERIFICA SE A RESOLUÇÃO NOS RETORNA UM INTEGRALIDADE E CASO NOS RETORNE O PROGRAMA JA PARA AQUI
integralidade = True
for i in range(retorno[0]):
    if(modelo_raiz.vals_vars[i] > 0 or modelo_raiz.vals_vars[i] < 1):
        integralidade = False 
if(integralidade == True):
    val_var_global = resolucao_raiz[0]
    Z_global = resolucao_raiz[1]    
    print(val_var_global)
    print(Z_global)

# CASO NAO RETORNE UMA INTEGRALIDADE COMEÇAREMOS A TRATAR E RAMIFICAR O NÓS
if(integralidade == False):
    Ramificar(modelo_raiz,closest(modelo_raiz.vals_vars, 0.5))
    # CONTINUA FAZENDO POP DA PILHA E RESOLVENDO ENQUANTO TENHA NÓ NA PILHA
    while(len(pilha) > 0):
        modelo = pilha.pop()
        resolucao = Resolver(modelo)
        modelo.vals_vars = resolucao[0]
        modelo.z = resolucao[1]
        # TESTA SE A SOLUÇÃO É VIÁVEL
        if(resolucao[1] > 0):
            integralidade = True
            for i in range(modelo.qVar):
                if(modelo.vals_vars[i] > 0 and modelo.vals_vars[i] < 1):
                    integralidade = False
            # TESTA SE A SOLUÇÃO É INTEGRAL
            if(integralidade == True):
                # TESTA SE A SOLUÇÃO OBTIDA É MELHOR QUE A SOLUÇÃO ATUAL
                if(resolucao[1] > Z_global):
                    val_var_global = resolucao[0]
                    Z_global = resolucao[1]
                    print(resolucao[0])
                    print(resolucao[1])
            else:
                # TESTA SE TEREMOS QUE PODAR POR LIMITANTE
                if(resolucao[1] > Z_global):
                    Ramificar(modelo,closest(modelo.vals_vars, 0.5))

print(val_var_global)
print(Z_global) 
