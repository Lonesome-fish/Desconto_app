class CriarPedidoOutputDTO:
    """DTO para transportar o resultado do processamento do pedido."""
    def __init__(
        self,
        cliente: str,
        valor_original: float,
        valor_desconto: float,
        valor_final: float,
        tipo_desconto: str
    ):
        self.cliente = cliente
        self.valor_original = valor_original
        self.valor_desconto = valor_desconto
        self.valor_final = valor_final
        self.tipo_desconto = tipo_desconto