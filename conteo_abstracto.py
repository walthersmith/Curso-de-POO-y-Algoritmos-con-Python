"""
Conteo abstracto de operación
"""

def f(x):
    respuesta = 0 

    for i in range(1000):
        respuesta += 1 

    print(f'primer for: {respuesta}')
    for i in range(x):
        respuesta += x
    
    print(f'segundo for: {respuesta}')
    
    for i in range(x):
        for j in range(x):
            respuesta += 1 
            respuesta += 1
    return respuesta

if __name__ == "__main__":
    print('resultado:', f(1))