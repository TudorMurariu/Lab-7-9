from Reports import rapoarte
from Validators import Validator
from persoane import persoane
from evenimente import evenimente
from evenimente_service import evenimente_service
from persoane_service import persoane_service
from repo_persoane import persoane_repository
from repo_evenimente import eveniment_repository
from Validators import Validator
from Reports import rapoarte
import random

def get_command():
        txt = input("Introdu o comanda :\n")
        return txt

def read_person():
        personID = input("ID-ul persoanei : ")
        nume = input("Numele persoanei : ")
        adresa = input("Adresa persoanei : ")
        persoana = persoane(personID, nume, adresa)
        return persoana

def read_eveniment():
        ID = input("ID-ul : ")
        data = input("Data : ")
        timp = input("Timp : ")
        descriere = input("Descriere : ")
        eveniment = evenimente(ID, data, timp, descriere)
        return eveniment

def print_persoane(lista_persoane):
    try:
        string = ""
        for el in lista_persoane:
            string += str(el) + " \n"
        if string[-1] == '\n':
            string = string[0:-1] # fara ultimul element
        print(string)
    except:
        print("Lista este vida.")
        

def print_evenimente(lista_evenimente):
    try:
        string = ""
        for el in lista_evenimente:
            string += str(el) + " \n"
        if string[-1] == '\n':
            string = string[0:-1] # fara ultimul element
        print(string)
    except:
        print("Lista este vida.")

def desparete_eveniment_persoana(args, valid):
    if not valid.verifica_inscriere(args):
        print("Speficicati evenimentul in care vreti sa adaugati persoana.")
        return ("-1","-1")
    
    persoana_nume_ID = ""
    i = 1
    while i < len(args):
        if args[i] == "in" or args[i] == "la":
            persoana_nume_ID = args[1:i]
            break
        i += 1
    eveniment_ID = args[i+1:]
    return [persoana_nume_ID, eveniment_ID]

class Console:
    def __init__(self, lista_persoane, lista_evenimente, service_persoane, 
    service_evenimente, repo_persoane, repo_evenimente, inscrieri, raport, validator):
        self.lista_persoane = lista_persoane
        self.lista_evenimente = lista_evenimente
        self.service_persoane = service_persoane
        self.service_evenimente = service_evenimente
        self.repo_persoane = repo_persoane
        self.repo_evenimente = repo_evenimente
        self.validator = validator
        self.inscrieri = inscrieri
        self.raport = raport

    def populate(self):
        '''
        Populeaza lista cu niste valori initiale
        '''

        p1 = persoane("123","Andrei Alexandru"," corbului 11")
        self.service_persoane.adauga_persoane(p1,self.lista_persoane)
        p2 = persoane("6645","Matei Pop"," corbului 22")
        self.service_persoane.adauga_persoane(p2,self.lista_persoane)
        p3 = persoane("6798","Alex"," fabricii 3")
        self.service_persoane.adauga_persoane(p3,self.lista_persoane)
        p4 = persoane("1001","Gabi"," umbrei 5")
        self.service_persoane.adauga_persoane(p4,self.lista_persoane)
        p5 = persoane("13","Stefan Paslaru"," umbrei 17")
        self.service_persoane.adauga_persoane(p5,self.lista_persoane)

        e1 = evenimente("7","11.01.2022","11:33","descriere1")
        self.service_evenimente.adauga_evenimente(e1, self.lista_evenimente)
        e2 = evenimente("123246","01.11.2012","03:55","descriere2")
        self.service_evenimente.adauga_evenimente(e2, self.lista_evenimente)
        e3 = evenimente("6767","30.01.2011","10:00","descriere3")
        self.service_evenimente.adauga_evenimente(e3, self.lista_evenimente)
        e4 = evenimente("555","03.01.2020","09:30","descriere4")
        self.service_evenimente.adauga_evenimente(e4, self.lista_evenimente)
        e5 = evenimente("31","11.09.2022","12:15","descriere5")
        self.service_evenimente.adauga_evenimente(e5, self.lista_evenimente)

        print("Populated event and person lists.")

    def show_reports(self):
        r1 = self.raport.evenimente_cu_o_singura_persoana()
        r2 = self.raport.persoanele_cu_cele_mai_multe_evenimente()
        r3 = self.raport.primele_evenimente_cu_cei_mai_multi_participanti()
        r4 = self.raport.top_cele_3_evenimente()

        # raport 1 
        if r1 == []:
            print("Nu exista evenimente la care participa o singura persoana.")
        else : 
            print("Lista de evenimente la care participă o persoană ordonat alfabetic după descriere, după dată :")
            for el in r1:
                print(el)
        
        print("Persoane participante la cele mai multe evenimente :")
        for el in r2:
            print(el)
        num = len(self.inscrieri.getEvenimente(r2[0]))
        print(f"Numarul de evenimente este la care participa acestia este: {num} \n")

        print("Primele 20 de procente de evenimente cu cei mai mulți participanți (descriere, număr participanți)")
        for el in r3:
            print(el.descriere , len(self.inscrieri.getPersoane(el)))
        
        if r4[0] != -1:
            print("Prinmele 3 evenimente cu cele mai multei participanti sunt :")
            for el in r4:
                print(el , len(self.inscrieri.getPersoane(el)))
        else:
            print("Nu exista 3 evenimente")

    

    def Interfata(self):
        
        while True:
            command = get_command()
            args = command.split()
            
            if args[0] == "adauga":
                if len(args) == 1:
                    print("Specificati daca vreti sa adaugati un eveniment sau o persoana.")
                elif args[1] == "persoana":
                    persoana = read_person() 
                    self.service_persoane.adauga_persoane(persoana,self.lista_persoane)
                elif args[1] == "eveniment":
                    eveniment = read_eveniment()
                    self.service_evenimente.adauga_evenimente(eveniment,self.lista_evenimente)
                else:
                    print("Trebuie sa specificati daca vreti sa adaugati un eveniment sau o persoana.")

            elif args[0] == "sterge":
                if len(args) == 1:
                    print("Specificati daca vreti sa stergeti un eveniment sau o persoana.")
                elif len(args) == 2:
                    print("Specificati ID-ul sau numele evenimentului/persoanei pe care vreti sa il/o stergeti.")
                elif args[1] == "persoana":
                    self.service_persoane.sterge_persoane(args, self.lista_persoane)
                elif args[1] == "evenimentul":
                    self.service_evenimente.sterge_evenimente(args, self.lista_evenimente)

            elif args[0] == "modifica":
                if len(args) == 1:
                    print("Specificati daca vreti sa modificati un eveniment sau o persoana.")
                elif len(args) == 2:
                    print("Specificati ID-ul sau numele evenimentului/persoanei pe care vreti sa il/o modificati.")
                elif args[1] == "persoana":
                    self.service_persoane.modifica_persoane(args, self.lista_persoane)
                elif args[1] == "evenimentul":
                    self.service_evenimente.modifica_evenimente(args, self.lista_evenimente)

            elif args[0] == "cauta":
                if len(args) == 1:
                    print("Specificati daca trebuie afisat un eveniment sau o persoana")
                elif len(args) == 2:
                    print("Specificati ID-ul sau numele persoanei/evenimentului.")
                elif args[1] == "persoana":
                    persoanaCautata = self.repo_persoane.cauta_persoana(args, self.lista_persoane)
                    print_persoane([persoanaCautata])
                    #self.repo_persoane.print_lista_evenimente(persoanaCautata)
                    lst = self.inscrieri.getEvenimente(persoanaCautata)
                    if lst != None:
                        print("Evenimentele la care participa :")
                    for el in lst:
                        print(el.getID())
                elif args[1] == "evenimentul":
                    evenimentCautat = self.repo_evenimente.cauta_eveniment(args, self.lista_evenimente)
                    print_evenimente([evenimentCautat])
                    #self.repo_evenimente.print_lista_persoane(evenimentCautat)
                    lst = self.inscrieri.getPersoane(evenimentCautat)
                    if lst != None:
                        print("Persoanele care participa :")
                    for el in lst:
                        print(el.getpersonID())
                else:
                    print("Specificati daca trebuie afisata lista de evenimente sau cea de persoane.")

            elif args[0] == "inscrie":
                nume_ID_persoana,ID_eveniment = desparete_eveniment_persoana(args, self.validator)               

                ID_eveniment = ID_eveniment[0]
                nume_ID_persoana = nume_ID_persoana[0]

                if (nume_ID_persoana,ID_eveniment) == ("-1","-1"):
                    continue
                if not self.validator.isID(ID_eveniment):
                    print("ID eveniment incorect!")
                    continue
                persoanaCautata = self.repo_persoane.cauta_persoana(["", "", nume_ID_persoana], self.lista_persoane)
                evenimentCautat = self.repo_evenimente.cauta_eveniment(["", "",ID_eveniment], self.lista_evenimente)
                if persoanaCautata == None or evenimentCautat == None:
                    continue
                #self.repo_persoane.add_eveniment(persoanaCautata, evenimentCautat)
                #self.repo_evenimente.add_persoana(evenimentCautat, persoanaCautata)
                self.inscrieri.inscrie(persoanaCautata, evenimentCautat)

            elif command == "rapoarte" or args[0] == "rapoarte":
                self.show_reports()

            elif args[0] == "genereaza":
                if len(args) == 1:
                    print("Specificati numarul de elemente si tipul de elemente pe care vreti sa le generati.")
                elif len(args) == 2:
                    print("Specificati daca vreti sa generati evenimente sau persoane.")
                else:
                    if not self.validator.isNumber(args[1]):
                        print("Trebuie sa speficati numarul de generari.")
                        continue
                    elif args[2] == "persoane":
                        nr = int(args[1])
                        for i in range(nr):
                            persoanaX = self.service_persoane.genereaza_persoana()
                            self.service_persoane.adauga_persoane(persoanaX, self.lista_persoane)
                    elif args[2] == "evenimente":
                        nr = int(args[1])
                        for i in range(nr):
                            evenimentX = self.service_evenimente.genereaza_eveniment()
                            self.service_evenimente.adauga_evenimente(evenimentX, self.lista_evenimente)

            elif args[0] == "print":
                if len(args) == 1:
                    print("Specificati daca trebuie afisata lista de evenimente sau cea de persoane.")
                elif args[1] == "persoane":
                    print_persoane(self.lista_persoane)
                elif args[1] == "evenimente":
                    print_evenimente(self.lista_evenimente)
                else:
                    print("Specificati daca trebuie afisata lista de evenimente sau cea de persoane.")

            elif command == "populate" or args[0] == "populate":
                self.populate()

            elif command == "exit":
                break
