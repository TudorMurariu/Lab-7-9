import unittest
from Validators import Validator
from persoane import persoane
from persoane_service import persoane_service

class Teste_Service_Persoane(unittest.TestCase):
        def setUp(self) -> None:
            pass

        def test_adauga_persoane(self):
                valid = Validator([],[]) 
                service = persoane_service(valid)
                p1 = persoane("1352","Andrei","Corbului 13")
                p2 = persoane("552","Matei","Fabricii 9")
                p3 = persoane("789","Andrei","Cuza 14")
                new_p = persoane("555","Maria","Cluj?")
                l1 = [p1,p2,p3]
                service.adauga_persoane(new_p,l1)
                assert l1 == [p1,p2,p3,new_p]
                l2 = []
                service.adauga_persoane(new_p,l2)
                assert l2 == [new_p]
                service.adauga_persoane(p1,l2)
                assert l2 == [new_p,p1]

        def test_sterge_persoane(self):
                valid = Validator([],[])
                service = persoane_service(valid)
                p1 = persoane("1352","Andrei M","Corbului 13")
                p2 = persoane("552","Matei","Fabricii 9")
                p3 = persoane("789","Ana","Cuza 14")
                p4 = persoane("555","Maria","Cluj?")
                l1 = [p1,p2,p3,p4]
                service.sterge_persoane(["","","Ana"],l1)
                assert l1 == [p1,p2,p4]
                l2 = [p1,p2,p3,p4]
                service.sterge_persoane(["","","552"],l2)
                assert l2 == [p1,p3,p4]
                service.sterge_persoane(["","","Andrei M"],l2)
                assert l2 == [p3,p4]

unittest.main()