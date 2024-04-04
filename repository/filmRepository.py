class FilmRepository:
    def __init__(self):
        self.__filme = {}

    def getAllFilmRepo(self):
        '''
        returneaza o lista de filme
        :return: lista de obiecte de tipul Client
        '''

        return list(self.__filme.values())


    def getByIdFilmRepo(self, idFilm):
        '''

        returneaza angajatul dupa id-ul dat
        :param idAngajat: string
        :return: un obiect de tipul angajhat, daca exista unul cu id-ul dat, altfel None
        '''

        #return self.__clienti.get(idFilm, None)

        if idFilm in self.__filme :
            return self.__filme[idFilm]
        return None

    def adaugaFilmRepo(self, film):
        '''
        adauga un client in dictionar
        :param client: obiect de tipul client
        :return:
        '''

        if self.getByIdFilmRepo(film.getIdFilm()) is not None :
            raise KeyError ("Exista deja un agajat cu acest Id")
        self.__filme[film.getIdFilm()] = film


    def modificaFilmRepo(self, filmNou):
        '''
        modifica un client dupa id
        :param clientNou: obiect de tipul Client
        :return:
        '''
        if self.getByIdFilmRepo(filmNou.getByIdFilm) :
            raise KeyError("Nu exista nici un film cu id ul dat")
        self.__filme[filmNou.getIdFilm()] = filmNou

    def stergeFilmRepo(self, idFilm):
        '''
        sterge un client dupa id
        :param idFilm: str
        :return:
        '''

        if self.getByIdFilmRepo(idFilm) is None:
            raise KeyError("Nu exista niciun film  cu idul dat")
        self.__filme.pop(idFilm)
