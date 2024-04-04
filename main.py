from repository.clientRepository import ClientRepository
from service.ClientService import ClientService
from teste.testAll import testAll
from ui.consola import Consola


def main():
    testAll()
    clientRepository = ClientRepository()
    clientService = ClientService(clientRepository)
    consola = Consola(clientService)

    consola.meniu()

main()