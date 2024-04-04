from domeniu.client import Client
from repository.clientRepository import ClientRepository
def testAdaugaClientRepository() :
    clientRepository = ClientRepository()
    client = Client("1", "Simon", "Ana", "5123123", "f", 19)

    clientRepository.adaugaClientRepo(client)

    clienti = clientRepository.getAllClientRepo()

    assert len(clienti) == 1
    assert clienti[0].getIdClient() == "1"

    try:
        clientRepository.adaugaClientRepo(client)
        assert False
    except KeyError:
        ...

def testStergeClientRepo():
    clientRepository = ClientRepository()
    client = Client("1", "Simon", "Ana", "5123123", "f", 19)

    clientRepository.adaugaClientRepo(client)

    clientRepository.stergeClientRepo("1")

    assert len(clientRepository.getAllClientRepo()) == 0

    try :
        clientRepository.stergeClientRepo("1")
        assert False
    except KeyError:
        ...

def testModificaClientRepository():
        clientRepository = ClientRepository()
        client = Client("1", "Simon", "Ana", "5123123", "f", 19)
        client2 = Client("1", "Dodu", "Ana", "5123123", "f", 20)
        clientRepository.adaugaClientRepo(client)

        clientRepository.modificaClientRepo(client2)

        clienti = clientRepository.getAllClientRepo()
        assert clienti[0].getnumeClient()=="Dodu"