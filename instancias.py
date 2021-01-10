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

    #print(cord_1.dinstancia(cord_2))
    print(isinstance(cord_2,Coordenada))