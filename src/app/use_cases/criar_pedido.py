from src.app.entities.pedido import Pedido
from src.app.entities.desconto import DescontoNormal, DescontoVIP, DescontoPremium

class CriarPedido:
    def executar(self, cliente: str, valor_original: float, tipo_desconto: str) -> Pedido:
        if tipo_desconto.lower() == "normal":
            desconto = DescontoNormal()
        elif tipo_desconto.lower() == "vip":
            desconto = DescontoVIP()
        elif tipo_desconto.lower() == "premium":
            desconto = DescontoPremium()
        else:
            raise ValueError("Tipo de desconto inválido")
            
        return Pedido(cliente, valor_original, desconto)