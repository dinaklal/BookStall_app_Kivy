import pytest
from App import DbCon


#test DB connection
def test_db() :
        db = DbCon.DbCon()
        assert True  == True if db.get_user() else False
