import pytest
from sqlalchemy import Engine
from .connection import db_conncetion_handler

@pytest.mark.skip(reason="interacao com o banco")
def test_connect_to_db():
    assert db_conncetion_handler.get_engine() is None

    db_conncetion_handler.connect_to_db()
    db_engine = db_conncetion_handler.get_engine()

    assert db_engine is not None
    assert isinstance(db_engine, Engine)
