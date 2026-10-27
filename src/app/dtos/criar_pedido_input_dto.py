class CriarPedidoInputDTO:
    """DTO para transportar os dados de entrada necessários para criar um pedido."""
    def __init__(self, cliente: str, valor_original: float, tipo_desconto: str):
        self.cliente = cliente
        self.valor_original = valor_original
        self.tipo_desconto = tipo_desconto