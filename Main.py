from src.database.connection import DatabaseConnection
from src.repositories.pedido_repository import PedidoRepository
from src.services.pedido_service import PedidoService
from src.controllers.pedido_controller import PedidoController
from src.models.pedido import Pedido
from src.models.desconto import DescontoNormal, DescontoVIP, DescontoPremium

if __name__ == "__main__":
    # Injeção de dependências em cadeia
    database = DatabaseConnection()
    repo = PedidoRepository(database)
    service = PedidoService(repo)
    controller = PedidoController(service)

    # Criação de pedidos de teste
    pedido1 = Pedido("Cliente 1", DescontoNormal())
    pedido1.valor_original = 100.0

    pedido2 = Pedido("Cliente 2", DescontoVIP())
    pedido2.valor_original = 100.0

    pedido3 = Pedido("Cliente 3", DescontoPremium())
    pedido3.valor_original = 100.0

    # Execução das operações pelo Controller
    controller.adicionar_pedido(pedido1)
    controller.adicionar_pedido(pedido2)
    controller.adicionar_pedido(pedido3)

    controller.processar_pedidos()