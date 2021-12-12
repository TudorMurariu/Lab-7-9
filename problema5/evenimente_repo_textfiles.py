import random
import UI 
from evenimente import evenimente
from Validators import Validator
import string

def generator_descriere():
    nume = ""
    nr = random.randint(1,10) # numarul de prenume/nume de familie
    for i in range(nr):
        vocala = False
        len_nume = random.randint(2,6)

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

class evenimente_repo_textfiles:
    def __init__(self,validator):
        self.validator = validator
        with open("evenimente.txt",'w') as f:
            f.write('') #stergem tot continutul din fisier
            f.close()

    def get_evenimente(self, lista_evenimente):
        lista_evenimente = self.read_evenimente()
        return lista_evenimente
        
    def adauga_evenimente(self, eveniment, lista_evenimente):
        lista_evenimente = self.read_evenimente()
        try:
            if not self.validator.verifica_ID_e(eveniment.get_ID()):
                raise AssertionError("ID incorect !")
            if not self.validator.verifica_timp(eveniment.get_timp()):
                raise AssertionError("Timp incorect !")
            with open("evenimente.txt",'w') as f:
                for el in lista_evenimente:
                    f.write(str(el) + '\n')
                f.write(str(eveniment) + '\n')
                f.close()
        except AssertionError as e:
            print(e)

    def read_evenimente(self):
        lista_raspuns = []
        with open("evenimente.txt",'r') as f:
            for line in f:
                line = line.replace('(','')
                line = line.replace(')','')
                line = line.replace('\n','')
                properties = line.split(', ')
                lista_raspuns.append(evenimente(properties[0],properties[1],properties[2],properties[3]))
            f.close()
        return lista_raspuns

    def sterge_evenimente(self, args, lista_evenimente):
        lista_evenimente = self.read_evenimente()
        poz = -1
        try:
            poz = int(args[2])
            for i in range(len(lista_evenimente)):
                if lista_evenimente[i].get_ID() == args[2]:
                    del lista_evenimente[i]
                    with open("evenimente.txt",'w') as f:
                        for el in lista_evenimente:
                            f.write(str(el) + '\n')
                        f.close()
                    return
            print("Nu exista un eveniment cu acest ID.")
        except:
            print("Trebuie sa introduceti ID-ul evenimentului pe care vreti sa il stergeti.")

    def modifica_evenimente(self, args, lista_evenimente):
        lista_evenimente = self.read_evenimente()
        poz = -1
        try:
            poz = int(args[2])

            for i in range(len(lista_evenimente)):
                if lista_evenimente[i].get_ID() == args[2]:
                    new_eveniment = UI.read_eveniment()
                    while not self.validator.verifica_ID_e(new_eveniment.get_ID()) or  not self.validator.verifica_timp(new_eveniment.get_timp()):
                        print("Input incorect !\nIncearca din nou : ")
                        new_eveniment = UI.read_eveniment()
                    lista_evenimente[i].set_ID(new_eveniment.get_ID())
                    lista_evenimente[i].set_data(new_eveniment.get_data())
                    lista_evenimente[i].set_timp(new_eveniment.get_timp())
                    lista_evenimente[i].set_descriere(new_eveniment.get_descriere())
                    with open("evenimente.txt",'w') as f:
                        for el in lista_evenimente:
                            f.write(str(el) + '\n')
                        f.close()
                    return
            print("Nu exista un eveniment cu acest ID.")
        except:
            print("Trebuie sa introduceti ID-ul evenimentului pe care vreti sa il modificati.")

    def genereaza_eveniment(self):
        # generare ID
        ID = ""
        len_ID = random.randint(1,9) # lungime id
        for i in range(len_ID):
            x = str(random.randint(1,9))
            ID += x
        
        # generare data
        data = ""
        an = random.randint(1999,2030)
        luna = random.randint(1,12)
        if luna == 2 and an % 4 == 0:
            zi = random.randint(1,29)
        elif luna == 2:
            zi = random.randint(1,28)
        elif luna % 2 == 1 and luna <= 7:
            zi = random.randint(1,31)
        elif luna <= 7:
            zi = random.randint(1,30)
        elif luna % 2 == 1:
            zi = random.randint(1,30)
        else:
            zi = random.randint(1,31)
        
        data = str(zi) + '.' + str(luna) + '.' + str(an)

        # generare timp

        timp = ""

        ora = random.randint(0,23)
        if ora < 10:
            ora = '0' + str(ora)
        else: 
            ora = str(ora)

        minut = random.randint(0,59)
        if minut < 10:
            minut = '0' + str(minut)
        else: 
            minut = str(minut)

        timp = ora + ':' + minut

        # generare descriere  in alta limba ????

        descriere = generator_descriere()

        return evenimente(ID, data, timp, descriere)