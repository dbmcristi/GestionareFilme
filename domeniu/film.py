class Filme :

    def __init__(self, idFilm, titluFilm, descriereFilm, genFilm, durataFilm, statutFilm):
        self.__idFilm = idFilm
        self.__titluFilm = titluFilm
        self.__descriereFilm = descriereFilm
        self.__genFilm = genFilm
        self.__durataFilm = durataFilm
        self.__statutFilm = statutFilm

    #Getters
    def getIdFilm(self):
        return self.__idFilm

    def getTitluFilm(self):
        return self.__titluFilm

    def getDescriereFilm(self):
        return self.__descriereFilm

    def getGenFilm(self):
        return self.__genFilm

    def getDurataFilm(self):
        return self.__durataFilm

    def getStatutFilm(self):
        return self.__statutFilm

    #Setters
    def setIdFilm(self,idFilm):
        self.__idFilm = idFilm

    def setTitluFilm(self,titluFilm):
        self.__titluFilm = titluFilm

    def setDescriereFilm(self,descriereFilm):
        self.__descriereFilm = descriereFilm

    def setGenFilm(self,genFilm):
        self.__genFilm = genFilm

    def setDurataFilm(self,durataFilm):
        self.__durataFilm = durataFilm

    def setStatutFilm(self,statutFilm):
        self.__statutFilm = statutFilm

    def __str__(self):
        return f"id: {self.__idFilm}, Titlu Film: {self.__titluFilm}, Descriere Film: {self.__descriereFilm}, Gen Film: {self.__genFilm}, Durata : {self.__durataFilm},Statut Film: {self.__statutFilm}  "