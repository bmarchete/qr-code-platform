from flask import jsonify, send_file
from flask_pydantic import validate
from adapters.api.dtos.create_qr_code_dto import CreateQrCodeDto
from adapters.qr_code_generator.segno_qr_code_generator import SegnoQrCodeGeneratorAdapter
from domain.service.create_qr_code_service import CreateQrCodeService

@validate()
def create_qr_code(body: CreateQrCodeDto):

    try:

        g = CreateQrCodeService(create_qr_code=SegnoQrCodeGeneratorAdapter())
        result = g.create(body.uuid, body.value)
        return send_file(result, mimetype='image/svg+xml')
       
    
    except Exception as e:
        print(e)
        return jsonify({"error": "Internal Server Error"}), 500
