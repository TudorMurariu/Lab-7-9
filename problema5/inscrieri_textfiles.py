from persoane import persoane
from evenimente import evenimente

class inscrieri_textfiles:
    def __init__(self, lista_persone, lista_evenimente, repo_persoane, repo_evenimente):
        self.lista_persone = lista_persone
        self.lista_evenimente = lista_evenimente
        self.repo_persoane = repo_persoane
        self.repo_evenimente = repo_evenimente
        with open("inscrieri.txt",'w') as f:
            f.write('') #stergem tot continutul din fisier
            f.close()
    
    def inscrie(self, person, eveniment):
        with open("inscrieri.txt",'a') as f:
            f.write(person.get_personID() + '&' + eveniment.get_ID() + '\n')
            f.close()
    
    def getInscrieri(self):
        lista_inscrieri = []
        with open("inscrieri.txt",'r') as f:
            for line in f:
                line = line.replace('\n','')
                personID , evenimentID = line.split("&")
                persoanaCautata = self.repo_persoane.cauta_persoana(["","",personID], self.lista_persone)
                evenimentCautata = self.repo_evenimente.cauta_eveniment(["","",evenimentID], self.lista_evenimente)
                element = (persoanaCautata , evenimentCautata)
                lista_inscrieri.append(element)
        return lista_inscrieri

    
    def getEvenimente(self, person):
        lista_inscrieri = self.getInscrieri()
        lisat_raspuns = []
        for el in lista_inscrieri:
            if el[0].get_personID() == person.get_personID():
                lisat_raspuns.append(el[1])
        return lisat_raspuns

    def getPersoane(self, eveniment):
        lista_inscrieri = self.getInscrieri()
        lisat_raspuns = []
        for el in lista_inscrieri:
            if el[1].get_ID() == eveniment.get_ID():
                lisat_raspuns.append(el[0])
        return lisat_raspuns