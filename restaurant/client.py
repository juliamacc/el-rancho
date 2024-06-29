# imports do Python
from threading import Thread
from random import randint
from time import sleep
from restaurant.shared import tickets, crew_condition, orders, chef_condition, table, totem

# imports do projeto

"""
    Não troque o nome das variáveis compartilhadas, a assinatura e o nomes das funções.
"""
class Client(Thread):
    
    """ Inicializa o cliente."""
    def __init__(self, id):
        super().__init__()
        self._id = id
        self.ticket = None
        # Insira o que achar necessario no construtor da classe.

    """ Pega o ticket do totem."""
    def get_my_ticket(self):
        self.ticket = totem.get_ticket()
        print(f"[TICKET] - O cliente {self._id} pegou o ticket {self.ticket}.")

    """ Espera ser atendido pela equipe. """
    def wait_crew(self):
        with crew_condition:
            while self.ticket not in tickets.queue:
                print(f"[WAIT] - O cliente {self._id} está aguardando atendimento.")
                crew_condition.wait()

    
    """ O cliente pensa no pedido."""
    def think_order(self):
        print(f"[THINK] - O cliente {self._id} está pensando no que pedir.")
        sleep(randint(1, 3))

    """ O cliente faz o pedido."""
    def order(self):
        print(f"[ORDER] - O cliente {self._id} pediu algo.")
        with chef_condition:
            orders.put(self.ticket)
            chef_condition.notify()

    """ Espera pelo pedido ficar pronto. """
    def wait_chef(self):
        with chef_condition:
            while self.ticket not in orders.queue:
                print(f"[WAIT MEAL] - O cliente {self._id} está aguardando o prato.")
                chef_condition.wait()

    """
        O cliente reserva o lugar e se senta.
        Lembre-se que antes de comer o cliente deve ser atendido pela equipe, 
        ter seu pedido pronto e possuir um lugar pronto pra sentar. 
    """
    def seat_and_eat(self):
        print(f"[WAIT SEAT] - O cliente {self._id} está aguardando um lugar ficar livre.")
        table.seat(self._id)
        print(f"[SEAT] - O cliente {self._id} encontrou um lugar livre e sentou.")
        sleep(randint(1, 3))  # Simula o tempo de comer
        table.leave(self._id)

    """ O cliente deixa o restaurante."""
    def leave(self):
        print(f"[LEAVE] - O cliente {self._id} saiu do restaurante".format(self._id))
    
    """ Thread do cliente """
    def run(self):
        self.get_my_ticket()
        self.wait_crew()
        self.think_order()
        self.order()
        self.wait_chef()
        self.seat_and_eat()
        self.leave()