import pytest
from App import DbCon


#test DB connection
def test_db() :
        db = DbCon.DbCon()
        assert True  == True if db.get_user() else False


def test_add_item():
        db = DbCon.DbCon()
        db.add_item("book",7,8,"GST CLASS - B","Books","b")
