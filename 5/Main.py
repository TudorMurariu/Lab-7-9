import UI
from evenimente_service import evenimente_service
from persoane_service import persoane_service
from Validators import Validator
from persoane import persoane
from evenimente import evenimente
from repo_evenimente import eveniment_repository
from repo_persoane import persoane_repository
from Reports import rapoarte

lista_persoane = []
lista_evenimente = []

if __name__ == '__main__':
    valid = Validator(lista_persoane, lista_evenimente)
    persoane_service1 = persoane_service(valid)
    evenimente_service1 = evenimente_service(valid)
    repo_persoane1 = persoane_repository()
    repo_evenimente1 = eveniment_repository()
    raport1 = rapoarte(lista_persoane, lista_evenimente)
    
    console = UI.Console(lista_persoane, lista_evenimente, persoane_service1, evenimente_service1, repo_persoane1, repo_evenimente1, raport1, valid)
    console.Interfata()
