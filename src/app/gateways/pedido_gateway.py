import abc
from src.app.entities.pedido import Pedido

class IPedidoGateway(abc.ABC):
    @abc.abstractmethod
    def salvar(self, pedido: Pedido, tipo_desconto: str) -> None:
        pass

    @abc.abstractmethod
    def listar(self) -> list:
        pass