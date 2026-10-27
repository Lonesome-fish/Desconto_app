from src.app.use_cases.criar_pedido import CriarPedido

class PedidoController:
    """Controlador que gerencia as requisições de entrada e delega para o Use Case."""
    def __init__(self, criar_pedido_use_case: CriarPedido):
        self.criar_pedido_use_case = criar_pedido_use_case

    def criar_pedido(self, cliente: str, valor_original: float, tipo_desconto: str):
        return self.criar_pedido_use_case.executar(cliente, valor_original, tipo_desconto)

    def listar_pedidos(self):
        return self.criar_pedido_use_case.listar_pedidos()