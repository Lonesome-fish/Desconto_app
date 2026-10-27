from src.models.desconto import IDesconto

class Pedido:
    def __init__(self, cliente: str, desconto: IDesconto):
        self.cliente = cliente
        self.desconto = desconto
        self.valor_original = 0.0

    def valor_final(self, valor: float) -> float:
        self.valor_original = valor
        return self.valor_original - self.desconto.calcular(self.valor_original)