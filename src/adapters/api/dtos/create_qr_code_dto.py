from typing import Annotated
from pydantic import UUID4, BaseModel, Strict

class CreateQrCodeDto(BaseModel):
    uuid: Annotated[UUID4, Strict(False)]
    value: str
