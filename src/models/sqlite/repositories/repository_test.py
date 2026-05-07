import pytest
from src.models.sqlite.settings.connection import db_conncetion_handler
from .pets_repository import PetsRepository

# db_conncetion_handler.connect_to_db()


@pytest.mark.skip(reason="interacao com o banco")
def test_list_pets():
    repo = PetsRepository(db_conncetion_handler)
    response = repo.list_pets()
    print(response)


def test_delete_pet():
    name = "belinha"
    repo = PetsRepository(db_conncetion_handler)
    repo.delete_pets(name)
