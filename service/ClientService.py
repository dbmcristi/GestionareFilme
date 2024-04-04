from repository.clientRepository import ClientRepository
from domeniu.client import Client

class ClientService:
    def __init__(self,clientRepository : ClientRepository):
        self.__clientRepository = clientRepository

    def getAllClientiService(self):
        '''
        returneaza lista de angajati
        :return: o lista de obiecte de tipul angajat
        '''
        return self.__clientRepository.getAllClientRepo()

    def adaugaClientService(self, idClient, numeClient, prenumeClient, cnp, sex, varstaClient):
        '''
        adauga un client
        :param idClient: str
        :param numeClient: str
        :param prenumeClient: str
        :param cnp: str
        :param sex: str
        :param varstaClient: int
        :return:
        '''
        client = Client(idClient,numeClient, prenumeClient, cnp, sex, varstaClient)
        self.__clientRepository.adaugaClientRepo(client)

    def modificaClientService(self, idClient, numeClientNou, prenumeClientNou, cnpNou, sexNou, varstaClientNou):
        '''
        modifca un angajat dupa id
        :param idClient: str
        :param numeClient: str
        :param prenumeClient: str
        :param cnp: str
        :param sex: str
        :param varstaClient: int
        :return:
        '''

        clientNou = Client(idClient,numeClientNou,prenumeClientNou,cnpNou,sexNou,varstaClientNou)
        self.__clientRepository.modificaClientRepo(clientNou)

    def stergeClientService(self,idClient):
        '''
        sterge un Client dupa ID
        :param idClient: str
        :return:
        '''
        self.__clientRepository.stergeClientRepo(idClient)