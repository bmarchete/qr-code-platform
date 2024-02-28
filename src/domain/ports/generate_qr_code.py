
from abc import ABC, abstractmethod
from io import BytesIO

class CreateQrCodeBuffInterface(ABC):

    @abstractmethod
    def generate_buff_from_text(value: str) -> BytesIO:
        pass # pragma: no cover