from evenimente import evenimente
from persoane import persoane

class eveniment_repository:

    def __init__(self):
        pass
    
    def number_persons(self, event):
        return len(event.lista_persoane)

    def cauta_eveniment(self, args, lista_evenimente):
        try:
            poz = int(args[2])
            for i in range(len(lista_evenimente)):
                if lista_evenimente[i].ID == args[2]:
                    return lista_evenimente[i]
            print("Nu exista un eveniment cu acest ID.")
        except:
            print("Trebuie sa introduceti ID-ul evenimentului pe care il cautati.")
    
    def add_persoana(self, event, persoana):
        event.lista_persoane.append(persoana)

    def print_lista_persoane(self, event):
        string = ""
        for el in event.lista_persoane:
            string += el.personID + "  "
        print("Persoanele care participa : ",string)
        