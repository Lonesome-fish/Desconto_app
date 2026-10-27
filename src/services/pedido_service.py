from src.models.pedido import Pedido

class PedidoService:
    """Classe de serviço para processar pedidos e aplicar descontos."""
    def __init__(self):
        self.pedidos = []

    def adicionar_pedido(self, pedido: Pedido):
        self.pedidos.append(pedido)

    def processar_pedidos(self):
        for pedido in self.pedidos:
            valor_calculado = pedido.valor_final(pedido.valor_original)
            print(f"Cliente: {pedido.cliente}")
            print(f"Valor final: {valor_calculado}\n")