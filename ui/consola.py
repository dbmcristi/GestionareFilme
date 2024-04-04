from service.ClientService import ClientService


class Consola:
    def __init__(self, clientService : ClientService):
        self.__clientService = clientService

    def adaugaClientUI(self):
        try :
            idClient = input("Id client: ")
            numeClient = input("nume: ")
            prenumeClient = input("prenume: ")
            cnpClient = input ("cnp: ")
            sexClient = input ("sex: ")
            varstaClient = int(input("varsta client: "))
            self.__clientService.adaugaClientService(idClient,numeClient,prenumeClient,cnpClient,sexClient,varstaClient)
        except KeyError as e :
            print(e)

    def modificaClientUI(self):
        '''
        modifica client dupa id
        :return:
        '''
        try:
            idClient = input("Dati id ul angajatului ce trebuie modificat")
            numeClientNou = input("nume nou:")
            prenumeClientNou = input("prenume nou")
            cnpClientNou = input("cnp nou:")
            sexClientNou = input("sex nou:")
            varstaClientNou = int(input("varsta client nou: "))
            self.__clientService.modificaClientService(idClient,numeClientNou,prenumeClientNou,cnpClientNou,sexClientNou,varstaClientNou)
        except KeyError as e :
            print(e)

    def stergeClientUI(self):
        try:
            idClient = input("Id client de sters")
            self.__clientService.stergeClientService(idClient)
        except KeyError as e :
            print(e)

    def afiseazaEntitati(self,entitati):
        for entitate in entitati :
            print(entitate)

    def printMeniu(self):
        print("1. Adauga client")
        print("2. Modifica client")
        print("3. Sterge client")
        print("a. Afiseaza toti client")
        print("x. Iesire")

    def meniu(self):
        while True :
            self.printMeniu()
            optiune = input("Dati optiunea")
            if optiune == "1":
                self.adaugaClientUI()
            elif optiune == "2":
                self.modificaClientUI()
            elif optiune == "3":
                self.stergeClientUI()
            elif optiune == "a":
                self.afiseazaEntitati(self.__clientService.getAllClientiService())
            elif optiune == "x":
                break
            else:
                print("Optiune gresita, reincercati!")