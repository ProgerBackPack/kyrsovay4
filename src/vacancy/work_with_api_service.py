from abc import ABC, abstractmethod


class WorkWithAPIService(ABC):
    # @abstractmethod
    # def __connect_to_api(self):
    #     pass

    @abstractmethod
    def get_vacancies(self, param):
        pass