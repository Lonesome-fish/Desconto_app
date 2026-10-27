from src.app.entities.pedido import Pedido
from src.app.gateways.pedido_gateway import IPedidoGateway
from src.app.frameworks.database.memory_database import MemoryDatabase

class MemoryPedidoRepository(IPedidoGateway):
    """Adapter de repositório em memória que armazena os pedidos formatados em dicionário."""
    def __init__(self, database: MemoryDatabase):
        self.database = database

    def salvar(self, pedido: Pedido, tipo_desconto: str) -> None:
        self.database.pedidos.append({"pedido": pedido, "tipo_desconto": tipo_desconto})

    def listar(self) -> list:
        return self.database.pedidos