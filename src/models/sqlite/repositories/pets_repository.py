from typing import List
from sqlalchemy.exc import NoResultFound
from src.models.sqlite.entities.pets import PetsTabel


class PetsRepository:
    def __init__(self, db_conncetion) -> None:
        self.__db_connetion = db_conncetion

    def list_pets(self) -> List:
        with self.__db_connetion as database:
            try:
                pets = database.session.query(PetsTabel).all()
                return pets
            except NoResultFound:
                return []

    def delete_pets(self, name: str) -> None:
        with self.__db_connetion as database:
            try:
                (
                    database.session.query(PetsTabel)
                    .filter(PetsTabel.name == name)
                    .delete()
                )
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception
