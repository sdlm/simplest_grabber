import abc
from typing import Union


class Grabber(abc.ABC):

    @abc.abstractmethod
    def load_data(self) -> Union[dict, list]:
        """
        Получить данные из внешнего источника.
        """
        pass
