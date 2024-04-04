
from repository.filmRepository import FilmRepository
from domeniu.film import Filme

class ClientService:
    def __init__(self,filmRepository : FilmRepository):
        self.__filmRepository = filmRepository

    def getAllFilmeService(self):
        '''
        returneaza lista de angajati
        :return: o lista de obiecte de tipul angajat
        '''
        return self.__filmRepository.getAllFilmeRepo()

    def adaugaFilmService(self, idFilm, titluFilm,descriereFilm, genFilm, durataFilm, statutFilm  ):
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
        film  = Filme(idFilm,titluFilm,descriereFilm,genFilm,durataFilm,statutFilm)
        self.__filmRepository.adaugaFilmRepo(film)

    def stergeFilmService(self, idFilm,titluFilm,descriereFilm,genFilm,durataFilm,statutFilm):
        '''
        modifca un client dupa id
        :param idClient: str
        :param numeClient: str
        :param prenumeClient: str
        :param cnp: str
        :param sex: str
        :param varstaClient: int
        :return:
        '''

        film  = Filme(idFilm,titluFilm,descriereFilm,genFilm,durataFilm,statutFilm)
        self.__filmRepository.modificaFilmRepo(filmNou)

    def stergeFilmService(self,idFilm):
        '''
        sterge un film dupa ID
        :param idClient: str
        :return:
        '''
        self.__filmRepository.stergeFilmRepo(idFilm)