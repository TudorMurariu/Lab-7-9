import unittest
from Validators import Validator
from evenimente_service import evenimente_service
from evenimente import evenimente

class Test_Service_Evenimente(unittest.TestCase):
    def setUp(self) -> None:
        pass
        
    def test_adauga_evenimente():
            valid = Validator([],[])
            service = evenimente_service(valid)
            e1 = evenimente("7335","12 sep","12:33","DESCRIERE")
            e2 = evenimente("7777","20 oct","14:50","DESCRIERE")
            e3 = evenimente("990","15 ian","09:55","DESCRIERE")
            l1 = [e1,e2,e3]
            new_e = evenimente("111","1 iul","00:00","NEW")
            service.adauga_evenimente(new_e,l1)
            assert l1 == [e1,e2,e3,new_e]
            l2 = [e3,e2,e1]
            service.adauga_evenimente(new_e,l2)
            assert l2 == [e3,e2,e1,new_e]

    def test_sterge_evenimente():
            valid = Validator([],[]) 
            service = evenimente_service(valid)
            e1 = evenimente("7335","12 sep","12:33","DESCRIERE")
            e2 = evenimente("7777","20 oct","14:50","DESCRIERE")
            e3 = evenimente("990","15 ian","09:55","DESCRIERE")
            e4 = evenimente("100","3 feb","11:00","Descriere")
            l1 = [e1,e2,e3,e4]
            service.sterge_evenimente(["","","990"],l1)
            assert l1 == [e1,e2,e4]
            l2 = [e3,e4,e1]
            service.sterge_evenimente(["","","990"],l2)
            assert l2 == [e4,e1]

unittest.main()