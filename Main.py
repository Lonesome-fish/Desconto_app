from src.app.frameworks.database.memory_database import MemoryDatabase
from src.app.adapters.repositories.memory_pedido_repository import MemoryPedidoRepository
from src.app.use_cases.criar_pedido import CriarPedido
from src.app.adapters.controllers.pedido_controller import PedidoController
from src.app.presenters.pedido_presenter import PedidoPresenter

def main() -> None:
    database = MemoryDatabase()
    pedido_gateway = MemoryPedidoRepository(database)
    criar_pedido_use_case = CriarPedido(pedido_gateway)
    presenter = PedidoPresenter()

    controller = PedidoController(
        criar_pedido_use_case=criar_pedido_use_case,
        presenter=presenter
    )

    # Criação dos pedidos
    pedido1 = controller.criar_pedido("Cliente A", 100.0, "normal")
    pedido2 = controller.criar_pedido("Cliente B", 200.0, "premium")
    pedido3 = controller.criar_pedido("Cliente C", 300.0, "vip")

    print("Pedidos criados:")
    print(pedido1)
    print(pedido2)
    print(pedido3)

    print("\nPedidos salvos:")
    for pedido in controller.listar_pedidos():
        print(pedido)

if __name__ == "__main__":
    main()