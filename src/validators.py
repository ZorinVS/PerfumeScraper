from src.base import BaseValidator


class PageNumberValidator(BaseValidator[int]):
    """ Класс для валидации количества страниц, которое необходимо спарсить """

    @staticmethod
    def validate(value: int) -> int:
        """ Валидирует количество страниц """
        if not isinstance(value, int):
            raise TypeError('Number of pages must be an integer value')
        if not 0 < value < 100_000:
            raise ValueError('The number of pages must be between 0 and 100,000 (exclusive)')
        return value


class GoldAppleDataValidator(BaseValidator[dict]):
    """ Класс для валидации данных, собранных с Золотого яблока """

    @staticmethod
    def validate(value: dict) -> dict:
        """ Валидирует извлеченные данные """
        if not isinstance(value, dict):
            raise TypeError('Scraped data must be of dictionary type')
        return value
