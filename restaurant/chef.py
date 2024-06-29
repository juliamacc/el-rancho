# imports do Python
from threading import Thread
from time import sleep
from random import randint
from restaurant.shared import orders, chef_condition

"""
    Não troque o nome das variáveis compartilhadas, a assinatura e o nomes das funções.
"""
class Chef(Thread):
    
    def __init__(self):
        super().__init__()
        # Insira o que achar necessario no construtor da classe.

    """ Chef prepara um dos pedido que recebeu do membro da equipe."""
    def cook(self, ticket):
        print(f"[COOKING] - O chefe está preparando o pedido para a senha {ticket}.")
        sleep(randint(1, 5))

    """ Chef serve o pedido preparado."""
    def serve(self, ticket):
        print(f"[READY] - O chefe está servindo o pedido para a senha {ticket}.")
    
    """ O chefe espera algum pedido vindo da equipe."""
    def wait_order(self):
        with chef_condition:
            while orders.empty():
                print("O chefe está esperando algum pedido.")
                chef_condition.wait()

    """ Thread do chefe."""
    def run(self):
        while True:
            self.wait_order()
            with chef_condition:
                if orders.empty():
                    break
                ticket = orders.get()
            self.cook(ticket)
            self.serve(ticket)