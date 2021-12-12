from persoane import persoane
import UI
from Validators import Validator
import random
import string

def generator_nume():
    nume = ""
    nr = random.randint(1,4) # numarul de prenume/nume de familie
    for i in range(nr):
        vocala = False
        len_nume = random.randint(2,6)
        prima_litera = random.choice(string.ascii_uppercase)
        nume += prima_litera
        if prima_litera in ['A','E','I','O','U']:
            vocala = True

        for j in range(len_nume):
            litera = random.choice(string.ascii_lowercase)
            nume += litera
            if litera in ['a','e','i','o','u']:
                vocala = True
        
        if not vocala:
            litera = random.choice(['a','e','i','o','u'])
            nume += litera
        nume += " "
    return nume[:-1]

class persoane_service:
    def __init__(self, validator):
        self.validator = validator

    def get_persoane(self, lista_persoane):
            return lista_persoane

    def adauga_persoane(self, persoana, lista_persoane):
        try:
            if not self.validator.verifica_ID_p(persoana.get_personID()):
                raise AssertionError("ID incorect !")
            #if not Validators.valid.verifica_nume(persoana.get_nume()):
                #raise AssertionError("Numele trebuie sa aiba cel putin doua cuvinte !")
            # numele pot avea cifre si semne , ex : Lucas al 3-lea
            lista_persoane.append(persoana)
        except AssertionError as e:
            print(e)

    def sterge_persoane(self, args, lista_persoane):
        poz = -1
        try:
            poz = int(args[2])
            for i in range(len(lista_persoane)):
                if lista_persoane[i].get_personID() == args[2]:
                    del lista_persoane[i]
                    return
            print("Nu exista o persoana cu acest ID.")
        except:
            numeCitit = ""
            for el in args[2:]:
                numeCitit = numeCitit + el + " "
            numeCitit = numeCitit[0:-1]

            for i in range(len(lista_persoane)):
                if lista_persoane[i].nume == numeCitit:
                    del lista_persoane[i]
                    return
            print("Nu exista o persoana cu acest nume.")
 
    def get_new_person(self): # o functie recursiva
        '''
            Functia primeste o persoana de la utilizator,
            verifica daca datele persoanei sunt corecte:
                Daca sunt corecte returneaza persoana
                Altfel afiseaza un mesaj de eroare si se apeleaza din nou
        '''
        new_person = UI.read_person()
        if not self.validator.verifica_ID_p(new_person.get_personID()):
            print("ID incorect !\nIncearca din nou : ")
            new_person = self.get_new_person()
        return new_person


    def modifica_persoane(self, args, lista_persoane):
        try:
            poz = int(args[2])
            for i in range(len(lista_persoane)):
                if lista_persoane[i].personID == args[2]:
                    new_person = self.get_new_person()
                    lista_persoane[i].set_personID(new_person.get_personID())
                    lista_persoane[i].set_nume(new_person.get_nume())
                    lista_persoane[i].set_adresa(new_person.get_adresa())
                    return
            print("Nu exista o persoana cu acest ID.")
        except:
            numeCitit = ""
            for el in args[2:]:
                numeCitit = numeCitit + el + " "
            numeCitit = numeCitit[0:-1]
            
            for i in range(len(lista_persoane)):
                if lista_persoane[i].nume == numeCitit:
                    new_person = UI.read_person()
                    while not self.validator.verifica_ID(new_person.get_personID()):
                        print("ID incorect !\nIncearca din nou : ")
                        new_person = UI.read_person()
                    lista_persoane[i].set_personID(new_person.get_personID())
                    lista_persoane[i].set_nume(new_person.get_nume())
                    lista_persoane[i].set_adresa(new_person.get_adresa())
                    return 
            print("Nu exista o persoana cu acest nume.")

    def genereaza_persoana(self):

        # generare ID
        personID = ""
        len_ID = random.randint(1,9) # lungime id
        for i in range(len_ID):
            x = str(random.randint(1,9))
            personID += x

        # generare nume
        nume = generator_nume()

        # generare adresa
        nr = random.randint(1,230)
        strada = generator_nume()
        adresa = "strada " + strada + " nr. " + str(nr)

        return persoane(personID, nume, adresa)

