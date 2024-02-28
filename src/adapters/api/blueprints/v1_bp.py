from flask import Blueprint

from adapters.api.handlers.qr_code_handler import create_qr_code

v1 = Blueprint("routes", __name__, url_prefix="/v1")

v1.add_url_rule("create", methods=["POST"], view_func=create_qr_code)
