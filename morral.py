'''
El problema del morral

Imagina que eres un ladrón que entra a un museo pero tienes un gran problema, 
nada mas tienes una mochila pero hay muchísimas cosas mas de las que puedes cargar, 
por lo cual debes determinar cuales artículos puedes cargar y te entregaran el mayor valor posible.

Para este problema sabemos que no podemos dividir los artículos, 
por lo que nuestra primera aproximación sera evaluar los artículos
'''
def morral(tamano_morral, pesos, valores, n): # O(2**n)
    print('-'*50)
    print(f'n = {n}  tamano_morral {tamano_morral}')
    #caso base 
    if n == 0 or tamano_morral == 0:
        print('Ya no hay espacio en la mochila!')
        return 0

    print(f'pesos[ n -1 ] {pesos[ n -1 ] }')
    if pesos[ n -1 ] > tamano_morral:
        return morral(tamano_morral, pesos, valores, n-1)

    print('Evaluamos para tomar el maximo')
    return max(valores[n-1] + morral(tamano_morral - pesos[n-1], pesos, valores, n-1 ),
           morral(tamano_morral, pesos, valores, n-1 ))

if __name__ == '__main__':
    valores = [60, 100, 120]
    pesos = [10, 20, 30]
    tamano_morral = 25 
    print(f"tamano del morral inicial: {tamano_morral}")
    n = len(valores)

    resultado = morral(tamano_morral, pesos, valores, n)
    print(resultado)