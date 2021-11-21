class Validator:
    def __init__(self, lista_persoane, lista_evenimente):
        self.lista_persoane = lista_persoane
        self.lista_evenimente = lista_evenimente
    
    def isID(self, ID):
        if ID == None:
            return False
        try :
            test = int(ID)
            return True
        except:
            return False
    
    def isNumber(self, string):
        try :
            test = int(string)
            return str(test == string)
        except:
            return False

    def verifica_ID_p(self, ID):
        for el in self.lista_persoane:
            if el.personID == ID:
                return False

        if self.isID(ID):
            return True
        return False
    
    def verifica_ID_e(self, ID):
        for el in self.lista_evenimente:
            if el.ID == ID:
                return False

        if self.isID(ID):
            return True
        return False
    
    #def verifica_nume(self, nume): # Nu folosim verificare pentru nume
    #    return len(nume) >= 2

    def verifica_timp(self, ora):
        # verificam daca timpul este de forma :
        # ora:minut
        try :
            aux = ora.split(':')
            if int(aux[0]) > 23:
                return False
            elif int(aux[1]) > 59:
                return False
            elif len(ora) != 5:
                return False
            elif ora[2] != ':':
                return False
            return True
        except :
            return False
    
    def verifica_inscriere(self, args):
        return args.count("in") == 1 or args.count("la") == 1
        

            
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



test_verifica_ID()
test_verifica_timp()