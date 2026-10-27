from src.app.entities.pedido import Pedido
from src.app.entities.desconto import DescontoNormal, DescontoVIP, DescontoPremium
from src.app.gateways.pedido_gateway import IPedidoGateway

class CriarPedido:
    """Caso de uso responsável por criar, aplicar regras de desconto e salvar pedidos."""
    def __init__(self, pedido_gateway: IPedidoGateway):
        self.pedido_gateway = pedido_gateway

    def executar(self, cliente: str, valor_original: float, tipo_desconto: str) -> Pedido:
        if tipo_desconto.lower() == "normal":
            desconto = DescontoNormal()
        elif tipo_desconto.lower() == "vip":
            desconto = DescontoVIP()
        elif tipo_desconto.lower() == "premium":
            desconto = DescontoPremium()
        else:
            raise ValueError("Tipo de desconto inválido")

        pedido = Pedido(cliente, valor_original, desconto)
        self.pedido_gateway.salvar(pedido)
        return pedido

    def listar_pedidos(self) -> list[Pedido]:
        return self.pedido_gateway.listar()