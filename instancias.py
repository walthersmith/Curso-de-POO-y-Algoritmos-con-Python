class Coordenada:
    
    def __init__(self,x , y):
        self.x = x 
        self.y = y

    def dinstancia(self,otra_coordenada):
        #Euclidean geometry method
        x_diff = (self.x - otra_coordenada.x)**2
        y_diff = (self.y - otra_coordenada.y)**2

        return (x_diff + y_diff)**0.5

if __name__ == "__main__":
    cord_1 = Coordenada(3,30)
    cord_2 = Coordenada(4,8)

    print(cord_1.dinstancia(cord_2))
    print(isinstance(cord_2,Coordenada))

"""
Que ocurre en este programa?...

 Se inicializan en el __init__ los parametros  (x, y) en init para las dos objetos creados cord_1 y Cord_2:
    cord_1 = Coordenada(3,30) = (x, y) 
    cord_2 = Coordenada(4,8) = (x, y) 

Que ocurre en print(cord_1.dinstancia(cord_2))?

en el objeto coord_1 llamamos al metodo distancia()
luego pasamos com parametro aese metodo el segundo objeto cord_2, el cual dentro de el metodo distancia() lo llamamos 
otra_cordenada
como pasamos un objeto y no solo un valor  podemos hacer uso de los atributos  que tiene ese objeto  que serian (x,y)
otra_coordenada.x = 4
otra_coordenada.y = 8

y la operacion matematica que realizaria el metodo seria el siguiente:
x_diff = (3 - 4)**2 = 1
y_diff = (30 - 8)**2 = 484

ahora en el return la operancion seria 
return (x_diff + y_diff)**0.5  
(1 + 484)**(1/2) = 22.0227, y el  el resultado final seria su raiz cuadrada.

"""