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

def test_top_cele_3_evenimente():
    inscrieri1 = inscrieri()
    p1 = persoane("123","Andrei Alexandru"," corbului 11")
    p2 = persoane("6645","Matei Pop"," corbului 22")
    p3 = persoane("6798","Alex","fabricii 3")
    p4 = persoane("888","Andreea Rusu","unirii 73")
    p5 = persoane("319","Maria"," fabricii 68")
    p6 = persoane("71","Daria","umbrei 13")

    repo_evenimente1 = eveniment_repository()
    e1 = evenimente("7","11.09.2020","11:33","descriere1")
    e2 = evenimente("123246","11.09.2021","03:55","descriere2")
    e3 = evenimente("6767","11.08.2011","10:00","descriere3")   
    e4 = evenimente("555","11.09.2011","09:30","descriere4")
    e5 = evenimente("789","12.09.2011","11:32","descriere5")
    e6 = evenimente("787","12.09.2011","11:32","descriere6")
    e7 = evenimente("5123","12.09.2011","11:32","descriere7")
    e8 = evenimente("6542","12.09.2011","11:32","descriere8")
    e9 = evenimente("087","12.09.2011","11:32","descriere9")
    e10 = evenimente("909","12.09.2011","11:32","descriere10")

    inscrieri1.inscrie(p2,e1) #
    inscrieri1.inscrie(p2,e2)#
    inscrieri1.inscrie(p1,e2)
    inscrieri1.inscrie(p3,e3) #
    inscrieri1.inscrie(p1,e4)#
    inscrieri1.inscrie(p2,e4)
    inscrieri1.inscrie(p3,e4)
    inscrieri1.inscrie(p3,e5) #
    inscrieri1.inscrie(p1,e6) #
    inscrieri1.inscrie(p1,e7) #
    inscrieri1.inscrie(p1,e8) #
    inscrieri1.inscrie(p1,e9) #
    inscrieri1.inscrie(p1,e10) #
    inscrieri1.inscrie(p2,e10)
    inscrieri1.inscrie(p3,e10)
    inscrieri1.inscrie(p4,e10)

    r1 = rapoarte([p1, p2, p3, p4, p5, p6],[e1, e2, e3, e4, e5, e6, e7, e8, e9, e10],inscrieri1)
    lista_raspuns = r1.top_cele_3_evenimente()
    assert lista_raspuns == [e10 , e4 , e2]

def test_evenimente_cu_o_singura_persoana():
    inscrieri1 = inscrieri()
    #repo_persoane1 = persoane_repository()
    p1 = persoane("123","Andrei Alexandru"," corbului 11")
    p2 = persoane("6645","Matei Pop"," corbului 22")
    p3 = persoane("6798","Alex"," fabricii 3")

    repo_evenimente1 = eveniment_repository()
    e1 = evenimente("7","11.09.2020","11:33","descriere1")
    e2 = evenimente("123246","11.09.2021","03:55","descriere2")
    e3 = evenimente("6767","11.08.2011","10:00","descriere3")   
    e4 = evenimente("555","11.09.2011","09:30","descriere4")
    e5 = evenimente("789","12.09.2011","11:32","descriere1")
    e6 = evenimente("787","12.09.2011","11:32","descriere3")

    inscrieri1.inscrie(p2,e1) #
    inscrieri1.inscrie(p2,e2)
    inscrieri1.inscrie(p1,e2)
    inscrieri1.inscrie(p3,e3) #
    inscrieri1.inscrie(p1,e4)
    inscrieri1.inscrie(p2,e4)
    inscrieri1.inscrie(p3,e4)
    inscrieri1.inscrie(p3,e5) #
    inscrieri1.inscrie(p1,e6) #

    r1 = rapoarte([p1, p2, p3],[e1, e2, e3, e4, e5, e6],inscrieri1)

    lista_raspuns = r1.evenimente_cu_o_singura_persoana()
    assert lista_raspuns == [e3, e5, e6, e1]



def test_persoanele_cu_cele_mai_multe_evenimente():
    inscrieri1 = inscrieri()
    p1 = persoane("123","Andrei Alexandru"," corbului 11")
    p2 = persoane("6645","Matei Pop"," corbului 22")
    p3 = persoane("6798","Alex","fabricii 3")
    p4 = persoane("888","Andreea Rusu","unirii 73")
    p5 = persoane("319","Maria"," fabricii 68")
    p6 = persoane("71","Daria","umbrei 13")

    e1 = evenimente("7","11.09.2020","11:33","descriere1")
    e2 = evenimente("123246","11.09.2021","03:55","descriere2")
    e3 = evenimente("6767","11.08.2011","10:00","descriere3")   
    e4 = evenimente("555","11.09.2011","09:30","descriere4")
    e5 = evenimente("789","12.09.2011","11:32","descriere1")
    e6 = evenimente("787","12.09.2011","11:32","descriere3")

    inscrieri1.inscrie(p1,e1)#
    inscrieri1.inscrie(p1,e4)
    inscrieri1.inscrie(p1,e5)
    inscrieri1.inscrie(p1,e6)
    inscrieri1.inscrie(p2,e1)#
    inscrieri1.inscrie(p3,e1)#
    inscrieri1.inscrie(p3,e2)
    inscrieri1.inscrie(p3,e4)
    inscrieri1.inscrie(p3,e6)
    inscrieri1.inscrie(p4,e3)#
    inscrieri1.inscrie(p5,e1)#
    inscrieri1.inscrie(p5,e2)
    inscrieri1.inscrie(p5,e3)
    inscrieri1.inscrie(p5,e5)
    inscrieri1.inscrie(p6,e3)#
    inscrieri1.inscrie(p6,e4)

    r1 = rapoarte([p1, p2, p3, p4, p5, p6],[e1, e2, e3, e4, e5, e6],inscrieri1)
    lista_raspuns = r1.persoanele_cu_cele_mai_multe_evenimente()
    assert lista_raspuns == [p1, p3, p5]

def test_primele_evenimente_cu_cei_mai_multi_participanti(): #20%
    inscrieri1 = inscrieri()
    p1 = persoane("123","Andrei Alexandru"," corbului 11")
    p2 = persoane("6645","Matei Pop"," corbului 22")
    p3 = persoane("6798","Alex","fabricii 3")
    p4 = persoane("888","Andreea Rusu","unirii 73")
    p5 = persoane("319","Maria"," fabricii 68")
    p6 = persoane("71","Daria","umbrei 13")

    repo_evenimente1 = eveniment_repository()
    e1 = evenimente("7","11.09.2020","11:33","descriere1")
    e2 = evenimente("123246","11.09.2021","03:55","descriere2")
    e3 = evenimente("6767","11.08.2011","10:00","descriere3")   
    e4 = evenimente("555","11.09.2011","09:30","descriere4")
    e5 = evenimente("789","12.09.2011","11:32","descriere5")
    e6 = evenimente("787","12.09.2011","11:32","descriere6")
    e7 = evenimente("5123","12.09.2011","11:32","descriere7")
    e8 = evenimente("6542","12.09.2011","11:32","descriere8")
    e9 = evenimente("087","12.09.2011","11:32","descriere9")
    e10 = evenimente("909","12.09.2011","11:32","descriere10")

    inscrieri1.inscrie(p2,e1) #
    inscrieri1.inscrie(p2,e2)
    inscrieri1.inscrie(p1,e2)
    inscrieri1.inscrie(p3,e3) #
    inscrieri1.inscrie(p1,e4)
    inscrieri1.inscrie(p2,e4)
    inscrieri1.inscrie(p3,e4)
    inscrieri1.inscrie(p3,e5) #
    inscrieri1.inscrie(p1,e6) #
    inscrieri1.inscrie(p1,e7) #
    inscrieri1.inscrie(p1,e8) #
    inscrieri1.inscrie(p1,e9) #
    inscrieri1.inscrie(p1,e10) #
    inscrieri1.inscrie(p2,e10)
    inscrieri1.inscrie(p3,e10)
    inscrieri1.inscrie(p4,e10)

    r1 = rapoarte([p1, p2, p3, p4, p5, p6],[e1, e2, e3, e4, e5, e6, e7, e8, e9, e10],inscrieri1)
    lista_raspuns = r1.primele_evenimente_cu_cei_mai_multi_participanti()
    assert lista_raspuns == [e10, e4]

test_evenimente_cu_o_singura_persoana()
test_persoanele_cu_cele_mai_multe_evenimente()
test_primele_evenimente_cu_cei_mai_multi_participanti()
test_top_cele_3_evenimente()