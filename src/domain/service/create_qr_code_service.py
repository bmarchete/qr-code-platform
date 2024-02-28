from domain.model.qr_code import QrCode
from domain.ports.create_qr_code import CreateQrCodeInterface
from domain.ports.generate_qr_code import CreateQrCodeBuffInterface
from domain.ports.qr_code_repository import QrCodeRepositoryInterface

class CreateQrCodeService(CreateQrCodeInterface):
    

    def __init__(self, create_qr_code: CreateQrCodeBuffInterface = None, repository: QrCodeRepositoryInterface = None):
        self.generate_qr_code = create_qr_code
        self.create_qr_code_repository = repository

              
    def create(self, uuid: str, value:str) -> QrCode:
        buff = self.generate_qr_code.generate_buff_from_text(value)
        return buff

       