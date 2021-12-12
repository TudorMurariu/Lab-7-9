from persoane import persoane
from evenimente import evenimente

class persoane_repository:
    def __init__(self):
        pass

    def cauta_persoana(self, args, lista_persoane):
        try:
            x = int(args[2])
            for i in range(len(lista_persoane)):
                if lista_persoane[i].personID == args[2]:
                    return lista_persoane[i]
            print("Nu exista o persoana cu acest ID.")
        except: 
            numeCitit = ""
            for el in args[2:]:
                numeCitit = numeCitit + el + " " 
            numeCitit = numeCitit[0:-1]
            
            for i in range(len(lista_persoane)):
                if lista_persoane[i].nume == numeCitit:
                    return lista_persoane[i]

            print("Nu exista o persoana cu acest nume.")
