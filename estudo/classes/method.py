from abc import ABC, abstractmethod


class Logistics:
    def createTransport(self):
        pass

    def planDelivery(self):
        transport = self.createTransport()
        
        result = f"Logistics: Transporte sendo preparado... \n{transport.deliver()}"
        return result


class RoadLogistics(Logistics):

    def __init__(self, name):
        self.name = name

    def createTransport(self):
        return Truck(self.name)


class SeadLogistics(Logistics):

    def __init__(self, name):
        self.name = name

    def createTransport(self):
        return Ship(self.name)


class Transport(ABC):
    @abstractmethod
    def deliver(self):
        pass


class Truck(Transport):
    def __init__(self, name):
        self.name = name
        self.category = "truck"

    def deliver(self):
        result = (f"{self.category} preparando para entrega: {self.name}",
                  "Transporte terreo.... ")
        return result


class Ship(Transport):
    def __init__(self, name):
        self.name = name
        self.category = "ship"

    def deliver(self):
        result = (f"{self.category} preparando para entrega: {self.name}",
                  "Transporte maritimo.... ")
        return result


def client_code(logistics: Logistics):
    print(f"App: Carregando com {logistics.__class__.__name__}.",
          f"{logistics.planDelivery()}")


if __name__ == "__main__":
    client_code(RoadLogistics("caminhao1"))

    client_code(RoadLogistics("navio"))


#https://youtu.be/CTagrzz-GXs?si=ct92WuQ1tZlSm0WC