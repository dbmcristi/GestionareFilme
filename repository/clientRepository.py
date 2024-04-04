class ClientRepository:

    def __init__(self):
        self.__clienti = {} #__clienti este dictionarul din fundal


    def getAllClientRepo(self):
        '''
        returneaza o lista de clienti
        :return: lista de obiecte de tipul Client
        '''

        return list(self.__clienti.values())


    def getByIdClientRepo(self, idClient):
        '''

        returneaza angajatul dupa id-ul dat
        :param idAngajat: string
        :return: un obiect de tipul angajhat, daca exista unul cu id-ul dat, altfel None
        '''

        #return self.__clienti.get(idClient, None)

        if idClient in self.__clienti :
            return self.__clienti[idClient]
        return None

    def adaugaClientRepo(self, client):
        '''
        adauga un client in dictionar
        :param client: obiect de tipul client
        :return:
        '''

        if self.getByIdClientRepo(client.getIdClient()) is not None :
            raise KeyError ("Exista deja un agajat cu acest Id")
        self.__clienti[client.getIdClient()] = client


    def modificaClientRepo(self, clientNou):
        '''
        modifica un client dupa id
        :param clientNou: obiect de tipul Client
        :return:
        '''
        if self.getByIdClientRepo(clientNou.getIdClient()) is None:
            raise KeyError("Nu exista nici un client cu id ul dat")
        self.__clienti[ clientNou.getIdClient() ] = clientNou

    def stergeClientRepo(self, idClient):
        '''
        sterge un client dupa id
        :param idClient: str
        :return:
        '''

        if self.getByIdClientRepo(idClient) is None:
            raise KeyError("Nu exista niciun client  cu idul dat")
        self.__clienti.pop(idClient)
