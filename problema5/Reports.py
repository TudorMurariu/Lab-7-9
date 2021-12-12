from persoane import persoane
from evenimente import evenimente
from repo_persoane import persoane_repository
from repo_evenimente import eveniment_repository
from inscrieri import inscrieri


class rapoarte:
    def __init__(self, lista_persoane, lista_evenimente, inscrieri):
        self.lista_persoane = lista_persoane
        self.lista_evenimente = lista_evenimente
        self.inscrieri = inscrieri

    def numar_persoane(self, e):
        return len(self.inscrieri.getPersoane(e))

    def evenimente_cu_o_singura_persoana(self):
        '''
            Returneaza o lista cu toate evenimentele cu un singur participant
        sortate dupa data si apoi descriere
        '''
        lista_raspuns = []
        for el in self.lista_evenimente:
            if len(self.inscrieri.getPersoane(el)) == 1:
                lista_raspuns.append(el)

        lista_raspuns.sort()

        return lista_raspuns

    def persoanele_cu_cele_mai_multe_evenimente(self):
        lista_raspuns = []
        max = 0
        for el in self.lista_persoane:
            if len(self.inscrieri.getEvenimente(el)) > max:
                lista_raspuns = [el]
                max = len(self.inscrieri.getEvenimente(el))
            elif len(self.inscrieri.getEvenimente(el)) == max:
                lista_raspuns.append(el)

        return lista_raspuns

    def primele_evenimente_cu_cei_mai_multi_participanti(self):
        numar_evenimente = 20 * len(self.lista_evenimente) // 100
        if numar_evenimente < 1:
            numar_evenimente = 1
        lista_raspuns = self.lista_evenimente[:]
        lista_raspuns.sort(key=self.numar_persoane,reverse=True)
        return lista_raspuns[0:numar_evenimente] # <= 20% 

    def top_cele_3_evenimente(self):
        try:
            lista_raspuns = self.lista_evenimente.copy()
            lista_raspuns.sort(key=self.numar_persoane,reverse=True)
            
            return lista_raspuns[0:3] # primele 3
        except:
            return [-1]
        