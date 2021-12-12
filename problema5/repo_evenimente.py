from evenimente import evenimente
from persoane import persoane

class eveniment_repository:

    def __init__(self):
        pass

    def cauta_eveniment(self, args, lista_evenimente):
        try:
            poz = int(args[2])
            for i in range(len(lista_evenimente)):
                if lista_evenimente[i].ID == args[2]:
                    return lista_evenimente[i]
            print("Nu exista un eveniment cu acest ID.")
        except:
            print("Trebuie sa introduceti ID-ul evenimentului pe care il cautati.")
            