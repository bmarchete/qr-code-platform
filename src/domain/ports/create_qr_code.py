
from abc import ABC, abstractmethod
from domain.model.qr_code import QrCode

class CreateQrCodeInterface(ABC):

    @abstractmethod
    def create() -> QrCode:
        pass # pragma: no cover