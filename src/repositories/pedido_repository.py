from src.models.pedido import Pedido
from src.database.connection import DatabaseConnection

class PedidoRepository:
    """Classe de repositório para armazenar e gerenciar pedidos."""
    def __init__(self, database: DatabaseConnection):
        self.database = database

    def adicionar_pedido(self, pedido: Pedido):
        self.database.pedidos.append(pedido)

    def listar_pedidos(self):
        return self.database.pedidos