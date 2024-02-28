from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

from domain.model.qr_code import QrCode
from domain.ports.qr_code_repository import QrCodeRepositoryInterface

class SQLAlchemyQrCodeRepository(QrCodeRepositoryInterface):
    

    def __init__(self, database) -> None:
        self.database = database
        print(f"Initialized SQLAlchemyQrCodeRepository with database: {self.database}")


    def create_qr_code(self, travel_distance: QrCode) -> None:

        try:
            with sessionmaker(bind=self.database.engine)() as session:
                session.add()
                session.commit()
        except SQLAlchemyError as e:
            print(f"Error occurred during create: {e}")
            raise e