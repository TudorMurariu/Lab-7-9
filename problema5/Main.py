import UI
from evenimente_service import evenimente_service
from persoane_service import persoane_service
from Validators import Validator
from persoane import persoane
from evenimente import evenimente
from repo_evenimente import eveniment_repository
from repo_persoane import persoane_repository
from Reports import rapoarte
from inscrieri import inscrieri
from inscrieri_textfiles import inscrieri_textfiles
from persoane_repo_textfile import persoane_repo_textfiles
from evenimente_repo_textfiles import evenimente_repo_textfiles

lista_persoane = []
lista_evenimente = []

if __name__ == '__main__':
    repo_persoane1 = persoane_repository()
    repo_evenimente1 = eveniment_repository()
    valid = Validator(lista_persoane, lista_evenimente)

    # In memorie
    #persoane_service1 = persoane_service(valid)
    #evenimente_service1 = evenimente_service(valid)
    #inscrieri1 = inscrieri()

    # In fisiere text
    inscrieri1 = inscrieri_textfiles(lista_persoane, lista_evenimente, repo_persoane1, repo_evenimente1)
    evenimente_service1 = evenimente_repo_textfiles(valid)
    persoane_service1 = persoane_repo_textfiles(valid)

    raport1 = rapoarte(lista_persoane, lista_evenimente, inscrieri1)
    console = UI.Console(lista_persoane, lista_evenimente, persoane_service1,
     evenimente_service1, repo_persoane1, repo_evenimente1, inscrieri1, raport1, valid)
    
    console.Interfata()
