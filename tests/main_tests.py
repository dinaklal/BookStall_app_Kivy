import pytest
from App import DbCon
from App.home import show_pop


#test DB connection
def test_db() :
        db = DbCon.DbCon()
        assert True  == True if db.get_user() else False


def test_add_item():
        db = DbCon.DbCon()
       # db.add_item("book",7,8,"GST CLASS - B","Books","b")
def test_pop_up():
        show_pop("test")

