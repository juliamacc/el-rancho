# Espaco reservado para voce inserir suas variaveis globais.
# Voce pode inserir como funcao (exemplo): 
# 
#  my_global_variable = 'Awesome value'
#  def get_my_global_variable():
#       global my_global_variable
#       return my_global_variable

from threading import Lock, Condition
import queue

tickets = queue.PriorityQueue()  # Fila de senhas de atendimento
orders = queue.Queue()  # Fila de pedidos para o chef
table = None  # Inicializado no main.py
totem = None  # Inicializado no main.py
ticket_lock = Lock()  # Lock para manipulação das senhas
order_lock = Lock()  # Lock para manipulação dos pedidos
chef_condition = Condition(order_lock)  # Condição para o chef esperar pedidos
crew_condition = Condition(ticket_lock)  # Condição para a equipe esperar clientes
seat_condition = Condition()  # Condição para os clientes esperarem assentos

def set_globals(t, tot):
    global table, totem
    table = t
    totem = tot