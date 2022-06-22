#from asyncio.windows_events import NULL
from mip import Model, xsum, maximize, CONTINUOUS

# FUNÇÃO QUE RESOLVE UM DADO NÓ(MODELO) E RETORNA OS VALORES DE X E Z
def Resolver(modelo):
    m = Model("")
    x = [m.add_var(var_type=CONTINUOUS, lb=0, ub=1) for i in range(modelo.qVar)]
    m.objective = maximize(xsum(modelo.obj[i] * x[i] for i in range(modelo.qVar)))
    for i in range(modelo.qRest):
        m += xsum(modelo.rest[i][j] * x[j] for j in range(modelo.qVar)) <= modelo.rest[i][modelo.qVar]
    
    # for k in range(modelo.qVar):
    #     m += (modelo.rest_1[k]*x[k] == 1)
    #     m += (modelo.rest_0[k]*x[k] == 0)

    for k in range(modelo.qVar):
        if(modelo.rest_1[k] == 1):
            m += x[k] == 1

    for k in range(modelo.qVar):
        if(modelo.rest_0[k] == 1):
            m += x[k] == 0
    

    m.optimize()

    vals_vars = []
    z = 0

    for k in range(modelo.qVar):
        vals_vars.append(x[k].x)
        try:  
            z = (modelo.obj[k] * x[k]).x + z
        except:
            z = -1
    return (vals_vars,z) 
