
"""
POLIMORFISMO 
es la capacidad de cambiar el comportamiento de una funcion 
de la superclase 

en python se debe escribir el mismo nombre del metodo en la subclase 
y con el mismo numero de parametros. 
"""

class Persona:
    
    def __init__(self,nombre):
        self.nombre = nombre

    def avanza(self):
        print('Ando Caminando')

    
class Ciclista(Persona):

    def __init__(self,nombre):
        super().__init__(nombre)

    def avanza(self):
        print('Ando moviendome en mi bicicleta')

def main():
    persona = Persona('David')
    persona.avanza()

    ciclista = Ciclista('Daniel')
    ciclista.avanza()

if __name__ == '__main__':
    main()