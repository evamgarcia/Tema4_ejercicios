import math 

def funcion(x):
    return math.exp(-x) -x

def calcular_biseccion(a,b,tol):
    if funcion(a)*funcion(b)>0:
        print("no hay raices en el intervalo")
    else:
        while abs(b-a)>tol:
            c = (a+b)/2.0
            if funcion(a)*funcion(c)<0:
                b=c
            else:
                a=c
            return c

def function(x):
    return math.exp(-x) -x

def calcular_secante(x0, x1, tol):
    while abs(x1-x0)>tol:
        x2 = x1-funcion(x1)*(x1-x0)/(funcion(x1) - funcion(x0))
        x0 =x1
        x1=x2
    return x2


def function(x):
    return math.exp(-x) -x 
def df(x):
    return -math.exp(-x) -1

def metodo_newton(x0, tol):
    while abs(funcion(x0))>tol:
        x0 = x0-funcion(x0)/df(x0)
        return x0

# comparar 

print("resultado de la biseecion: ", calcular_biseccion(10,10, 0.0001))
print("resultado de la secante: ", calcular_secante(10,10, 0.0001))
print("resultado del metodo newton: ", metodo_newton(10,10, 0.0001))
