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

class persoane_repo_textfiles:
    def __init__(self, validator):
        self.validator = validator
        with open("persoane.txt",'w') as f:
            f.write('') #stergem tot continutul din fisier
            f.close()

    def adauga_persoane(self, persoana, lista_persoane):
        lista_persoane = self.read_persoane()
        try:
            if not self.validator.verifica_ID_p(persoana.get_personID()):
                raise AssertionError("ID incorect !")
            #if not Validators.valid.verifica_nume(persoana.get_nume()):
                #raise AssertionError("Numele trebuie sa aiba cel putin doua cuvinte !")
            # numele pot avea cifre si semne , ex : Lucas al 3-lea
            with open("persoane.txt",'w') as f:
                for el in lista_persoane:
                    f.write(str(el) + '\n')
                f.write(str(persoana) + '\n')
                f.close()
        except AssertionError as e:
            print(e)

    def read_persoane(self):
        lista_raspuns = []
        with open("persoane.txt",'r') as f:
            for line in f:
                line = line.replace('(','')
                line = line.replace(')','')
                line = line.replace('\n','')
                properties = line.split(', ')
                lista_raspuns.append(persoane(properties[0],properties[1],properties[2]))
            f.close()
        return lista_raspuns
    
    def get_persoane(self, lista_persoane):
        return self.read_persoane()

    def sterge_persoane(self, args, lista_persoane):
        lista_persoane = self.read_persoane()
        poz = -1
        try:
            poz = int(args[2])
            ok = False

            for i in range(len(lista_persoane)):
                if lista_persoane[i].get_personID() == args[2]:
                    del lista_persoane[i]
                    ok = True
            with open("persoane.txt",'w') as f:
                for el in lista_persoane:
                    f.write(str(el) + '\n') 
                f.close()   
            if not ok:     
                print("Nu exista o persoana cu acest ID.")
        except:
            numeCitit = ""
            for el in args[2:]:
                numeCitit = numeCitit + el + " "
            numeCitit = numeCitit[0:-1]

            ok = False
            for i in range(len(lista_persoane)):
                if lista_persoane[i].nume == numeCitit:
                    del lista_persoane[i]
                    ok = True
            with open("persoane.txt",'w') as f:
                for el in lista_persoane:
                    f.write(str(el) + '\n') 
                f.close()        
            if not ok:
                print("Nu exista o persoana cu acest nume.")

    def modifica_persoane(self, args, lista_persoane):
        lista_persoane = self.read_persoane()
        try:
            poz = int(args[2])
            ok = False
            for i in range(len(lista_persoane)):
                if lista_persoane[i].personID == args[2]:
                    new_person = UI.read_person()
                    while not self.validator.verifica_ID_p(new_person.get_personID()):
                        print("ID incorect !\nIncearca din nou : ")
                        new_person = UI.read_person()
                    lista_persoane[i].set_personID(new_person.get_personID())
                    lista_persoane[i].set_nume(new_person.get_nume())
                    lista_persoane[i].set_adresa(new_person.get_adresa())
                    ok = True
            with open("persoane.txt",'w') as f:
                for el in lista_persoane:
                    f.write(str(el) + '\n') 
                f.close()  
                    
            if not ok:
                print("Nu exista o persoana cu acest ID.")
        except:
            numeCitit = ""
            for el in args[2:]:
                numeCitit = numeCitit + el + " "
            numeCitit = numeCitit[0:-1]
            ok = False
            for i in range(len(lista_persoane)):
                if lista_persoane[i].nume == numeCitit:
                    new_person = UI.read_person()
                    while not self.validator.verifica_ID(new_person.get_personID()):
                        print("ID incorect !\nIncearca din nou : ")
                        new_person = UI.read_person()
                    lista_persoane[i].set_personID(new_person.get_personID())
                    lista_persoane[i].set_nume(new_person.get_nume())
                    lista_persoane[i].set_adresa(new_person.get_adresa())
                    ok = True
            with open("persoane.txt",'w') as f:
                for el in lista_persoane:
                    f.write(str(el) + '\n') 
                f.close()  
            
            if not ok:
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


