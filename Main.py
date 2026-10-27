from src.models.desconto import DescontoNormal, DescontoVIP, DescontoPremium
from src.models.pedido import Pedido
from src.services.pedido_service import PedidoService

if __name__ == "__main__":
    # 1. Instanciar a camada de serviço
    service = PedidoService()

    # 2. Criar pedidos com diferentes categorias de desconto
    pedido1 = Pedido("Leonardo", DescontoVIP())
    pedido1.valor_original = 100.0

    pedido2 = Pedido("Maria", DescontoNormal())
    pedido2.valor_original = 200.0

    pedido3 = Pedido("Carlos", DescontoPremium())
    pedido3.valor_original = 300.0

    # 3. Adicionar pedidos ao serviço
    service.adicionar_pedido(pedido1)
    service.adicionar_pedido(pedido2)
    service.adicionar_pedido(pedido3)

    # 4. Processar e exibir os pedidos
    print("--- PROCESSANDO PEDIDOS NA CAMADA DE SERVIÇO ---\n")
    service.processar_pedidos()