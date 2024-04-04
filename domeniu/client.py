class Client:

    def __init__(self, idClient , numeClient, prenumeClient , cnp, sex, varstaClient ) :
        self.__idClient = idClient
        self.__numeClient = numeClient
        self.__prenumeClient = prenumeClient
        self.__cnp = cnp
        self.__sex = sex
        self.__varstaClient = varstaClient

    #Getters
    def getIdClient(self):
        return self.__idClient

    def getnumeClient(self):
        return self.__numeClient

    def getPrenumeClient(self):
        return self.__prenumeClient

    def getCNPClient(self):
        return self.__cnp

    def getSexClient(self):
        return self.__sex

    def getVarstaClient(self):
        return self.__varstaClient


    #Setters
    def setIdClient(self,idClient):
        self.__idClient = idClient


    def setNumeClient(self, numeClient):
        self.__numeClient = numeClient

    def setPrenumeClient(self, prenumeClient):
        self.__prenumeClient=prenumeClient

    def setCNP(self,cnp):
        self.__cnp = cnp

    def setSex(self,sex):
        self.__sex = sex

    def setVarstaClient(self, varstaClient):
        self.__varstaClient = varstaClient


    def __str__(self):
        return f"id: {self.__idClient}, nume: {self.__numeClient}, prenume: {self.__numeClient}, cnp: {self.__cnp}, sex: {self.__sex},varsta: {self.__varstaClient}  "