
"""
Descomposicion 
es la forma en la que podemos partir enfrentarnos a un problema 
partiendo este en partes mas pequeñas  es las cuales nos podemos cocentrar 

se realiza un ejemplo de un automovil  y la forma en como se podria representar 
"""

class Automovil:
    def __init__(self,modelo,marca,color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado = 'en_reposo'
        self._motor = None

    def acelerar(self,tipo='despacio'):
        if tipo == 'rapida':
            self._motor.inyecta_gasolina(10)
        else:
            self._motor.inyecta_gasolina(3)
        
        self._estado = 'en movimiento'
        

class Motor:

    def __init__ (self,cilindros, tipo='gasolina'):
        self.cilindros = cilindros
        self.tipo = tipo 
        self._temperatura = 0
        self._capacidad   = 0
        self._estado      = 'sin gasolina'

    def inyecta_gasolina(self,cantidad):
        
        self.gasolina -= cantidad
        if self.gasolina <= 0:
            self._estado = 'sin gasolina'
        
        
