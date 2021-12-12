from Validators import Validator
import unittest

class Teste_validari(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_verifica_inscriere():
        valid = Validator([],[])
        assert valid.verifica_inscriere(["ana","in","12312"]) == True
        assert valid.verifica_inscriere(["ana","in","12312"]) == True
        assert valid.verifica_inscriere(["ana","in","123","in","12312"]) == False
        assert valid.verifica_inscriere(["ana","adwjdan","dawuhdwau","12312"]) == False

    def test_verifica_ID():
        valid = Validator([],[])
        assert valid.isID("01230511") == True
        assert valid.isID("ana") == False
        assert valid.isID("1234.79") == False
        assert valid.isID("00000000000") == True
        assert valid.isID("123145;?980") == False
        assert valid.isID("13") == True

    def test_verifica_timp():
        valid = Validator([],[])
        assert valid.verifica_timp("12:55") == True
        assert valid.verifica_timp("25:33") == False
        assert valid.verifica_timp("09:66") == False
        assert valid.verifica_timp("03:08") == True
