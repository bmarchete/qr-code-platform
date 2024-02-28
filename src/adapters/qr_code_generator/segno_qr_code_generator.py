import io
import segno
from domain.ports.generate_qr_code import CreateQrCodeBuffInterface

class SegnoQrCodeGeneratorAdapter(CreateQrCodeBuffInterface):


    def generate_buff_from_text(self, value: str) -> io.BytesIO:
       
        buff = io.BytesIO()
        segno.make(value, micro=False).save(buff, kind='svg', scale=4)
        buff.seek(0)
        return buff