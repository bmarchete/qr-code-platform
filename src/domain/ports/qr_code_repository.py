from abc import ABC, abstractmethod

from domain.model.qr_code import QrCode

class QrCodeRepositoryInterface(ABC):

    @abstractmethod
    def create_qr_code(self, qr_code: QrCode) -> None:
        pass # pragma: no cover