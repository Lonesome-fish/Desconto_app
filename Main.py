from src.app.frameworks.database.memory_database import MemoryDatabase
from src.app.adapters.repositories.memory_pedido_repository import MemoryPedidoRepository
from src.app.use_cases.criar_pedido import CriarPedido
from src.app.adapters.controllers.pedido_controller import PedidoController

def main() -> None:
    # 1. Infraestrutura e Adapters
    database = MemoryDatabase()
    pedido_gateway = MemoryPedidoRepository(database)

    # 2. Injeção de dependência do Use Case
    criar_pedido_use_case = CriarPedido(pedido_gateway)

    # 3. Controller
    controller = PedidoController(criar_pedido_use_case)

    # 4. Execução dos fluxos de criação de pedidos
    pedido1 = controller.criar_pedido("Cliente A", 100.0, "normal")
    pedido2 = controller.criar_pedido("Cliente B", 100.0, "vip")
    pedido3 = controller.criar_pedido("Cliente C", 100.0, "premium")

    # 5. Exibição dos resultados
    print("Pedidos criados:")
    print(pedido1.cliente, pedido1.valor_original, pedido1.valor_final())
    print(pedido2.cliente, pedido2.valor_original, pedido2.valor_final())
    print(pedido3.cliente, pedido3.valor_original, pedido3.valor_final())

if __name__ == "__main__":
    main()