class persoane:
    def __init__(self, personID, nume, adresa):
        self.personID = personID
        self.nume = nume
        self.adresa = adresa
        self.lista_evenimente = []

    def __str__(self):
        return '(' + str(self.personID) + ", " + self.nume + ", " + self.adresa + ')'
    
    def set_personID(self,personID):
        self.personID = personID

    def set_nume(self,nume):
        self.nume = nume

    def set_adresa(self,adresa):
        self.adresa = adresa

    def get_personID(self):
        return self.personID
    
    def get_nume(self):
        return self.nume

    def get_adresa(self):
        return self.adresa

