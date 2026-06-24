import sys
from pathlib import Path

print("PYTHON:", sys.executable)
print("PATH:", sys.path)

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import pytest
import os 
import sqlite3
from database.database import connect_db, create_table
from app import app
import database.database as db
TEST_DB = "test_member.db"
@pytest.fixture
def client():
    app.config["TESTING"] = True
    def test_connect_db():
        return sqlite3.connect(TEST_DB)
    db.connect_db = test_connect_db
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)
    create_table()
    with app.test_client() as client :
        yield client
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)
