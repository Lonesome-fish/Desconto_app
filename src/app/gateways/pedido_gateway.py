import abc
from src.app.entities.pedido import Pedido

class IPedidoGateway(abc.ABC):
    @abc.abstractmethod
    def salvar(self, pedido: Pedido) -> None:
        pass

    @abc.abstractmethod
    def listar(self) -> list[Pedido]:
        pass