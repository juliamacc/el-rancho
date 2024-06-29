
"""
    Não troque o nome das variáveis compartilhadas, a assinatura e o nomes das funções.
"""
from threading import Condition

class Table:
    def __init__(self, number):
        self._number = number
        self.available_seats = number
        self.condition = Condition()

    def seat(self, client):
        with self.condition:
            while self.available_seats == 0:
                print(f"[WAIT SEAT] - O cliente {client} está aguardando um lugar ficar livre.")
                self.condition.wait()
            self.available_seats -= 1
            print(f"[SEAT] - O cliente {client} encontrou um lugar livre e sentou.")

    def leave(self, client):
        with self.condition:
            self.available_seats += 1
            print(f"[LEAVE] - O cliente {client} deixou a mesa.")
            self.condition.notify()