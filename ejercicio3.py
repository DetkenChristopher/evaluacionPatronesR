from abc import ABC, abstractmethod


# Factory Method
class cafe:
    def __init__(self, tipo, precio):
        self.tipo = tipo
        self.precio = precio

class te:
    def __init__(self, tipo, precio):
        self.tipo = tipo
        self.precio = precio
        
class Jugo:
    def __init__(self, tipo, precio):
        self.tipo = tipo
        self.precio = precio
        
class CafeteriaFactory:
    def crear_bebida(self, bebida_tipo, tipo, precio):
        if bebida_tipo == "cafe":
            return cafe(tipo, precio)
        elif bebida_tipo == "te":
            return te(tipo, precio)
        elif bebida_tipo == "jugo":
            return Jugo(tipo, precio)
        else:
            raise ValueError(f"Tipo de bebida desconocido: {bebida_tipo}")

# Decorator

class Comlementos(ABC):
    @abstractmethod
    def agregar(self, complemento):
        pass
    
class Leche(Comlementos):
    def agregar(self, complemento):
        print("Agregando leche a la bebida {self.bebida}")

class Azucar(Comlementos):
    def agregar(self, complemento):
        print("Agregando azucar a la bebida {self.bebida}")
        
class canela(Comlementos):
    def agregar(self, complemento, bebida):
        print("Agregando canela a la bebida {self.bebida}")
        
class NotificadorComplementos:
    def __init__(self, bebida):
        self.bebida = bebida
        self.complementos = []

    def agregar_complemento(self, complemento):
        self.complementos.append(complemento)
        complemento.agregar(self.bebida)

#Observer

class NotificadorCajero(ABC):
    @abstractmethod
    def actualizar(self, mensaje):
        pass

class Pedido:
    def __init__(self):
        self.observadores = []
    
    def agregar_observador(self, observador):
        self.observadores.append(observador)
        
    def remover_observador(self, observador):
        self.observadores.remove(observador)
        
    def notificar_observadores(self, mensaje):
        for observador in self.observadores:
            observador.actualizar(mensaje)
    
    def realizar_pedido(self, bebida):
        mensaje = f"Nuevo pedido: {bebida.tipo} - ${bebida.precio}"
        self.notificar_observadores(mensaje)
        
class Cajero(NotificadorCajero):
    def __init__(self, nombre):
        self.nombre = nombre
    
    def actualizar(self, mensaje):
        print(f"Cajero {self.nombre} ha recibido la notificación: {mensaje}")
        

#ejemplo 
factory = CafeteriaFactory()
cafe1 = factory.crear_bebida("cafe", "Espresso", 2.5)
te1 = factory.crear_bebida("te", "Verde", 1.5)
jugo1 = factory.crear_bebida("jugo", "Naranja", 3.0)

notificador_complementos = NotificadorComplementos(cafe1)
leche = Leche()
azucar = Azucar()
canela = canela()

notificador_complementos.agregar_complemento(leche)
notificador_complementos.agregar_complemento(azucar)

pedido = Pedido()
cajero1 = Cajero("Juan")
cajero2 = Cajero("Maria")

pedido.agregar_observador(cajero1)
pedido.agregar_observador(cajero2)

pedido.realizar_pedido(cafe1)
pedido.realizar_pedido(te1)
pedido.realizar_pedido(jugo1)
