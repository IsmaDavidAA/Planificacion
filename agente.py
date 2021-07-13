
class Agente():
    def __init__(self, n):
        print('Agente: '+ n)
        self.ocupado = 0
        self.name = n
    def dec(self):
        self.ocupado = self.ocupado - 1
        if self.ocupado < 0:
            self.ocupado = 0
    def ocupar(self, o):
        self.ocupado = o
    def estadoOcupado(self):
        if self.ocupado > 0:
            return "Ocupado"
        else:
            return "Libre"