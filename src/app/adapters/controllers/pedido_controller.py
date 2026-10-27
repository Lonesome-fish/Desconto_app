from src.app.use_cases.criar_pedido import CriarPedido
from src.app.dtos.criar_pedido_input_dto import CriarPedidoInputDTO
from src.app.presenters.pedido_presenter import PedidoPresenter

class PedidoController:
    """Controller integrado com DTOs de entrada e Presenter na saída."""
    def __init__(self, criar_pedido_use_case: CriarPedido, presenter: PedidoPresenter):
        self.criar_pedido_use_case = criar_pedido_use_case
        self.presenter = presenter

    def criar_pedido(self, cliente: str, valor_original: float, tipo_desconto: str):
        input_dto = CriarPedidoInputDTO(
            cliente=cliente,
            valor_original=valor_original,
            tipo_desconto=tipo_desconto
        )
        output_dto = self.criar_pedido_use_case.executar(input_dto)
        return self.presenter.apresentar(output_dto)

    def listar_pedidos(self):
        output_dtos = self.criar_pedido_use_case.listar_pedidos()
        return self.presenter.apresentar_lista(output_dtos)