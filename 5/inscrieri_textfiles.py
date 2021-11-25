
class inscrieri_textfiles:
    def __init__(self):
        self.lista_inscrieri = []
    
    def inscrie(self, person, eveniment):
        self.lista_inscrieri.append((person, eveniment))
    
    def getInscrieri(self):
        return self.lista_inscrieri
    
    def getEvenimente(self, person):
        lisat_raspuns = []
        for el in self.lista_inscrieri:
            if el[0].get_personID() == person.get_personID():
                lisat_raspuns.append(el[1])
        return lisat_raspuns

    def getPersoane(self, eveniment):
        lisat_raspuns = []
        for el in self.lista_inscrieri:
            if el[1].get_ID() == eveniment.get_ID():
                lisat_raspuns.append(el[0])
        return lisat_raspuns