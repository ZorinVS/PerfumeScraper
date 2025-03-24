from typing import Any

import pytest

from src.validators import GoldAppleDataValidator, PageNumberValidator


# ==== Тесты для GoldAppleDataValidator ====

def test_gold_apple_data_validator_for_correct_value() -> None:
    """ Тест успешной валидации типа извлеченных данных """
    scrapped_data = {'link': [], 'name': []}
    assert GoldAppleDataValidator.validate(scrapped_data) == scrapped_data


def test_gold_apple_data_validator_for_invalid_value_type() -> None:
    """ Тест валидации передачи извлеченных данных некорректного типа """
    scrapped_data: Any = [{'link': '', 'name': ''}]
    with pytest.raises(TypeError) as exc_info:
        GoldAppleDataValidator.validate(scrapped_data)
    expected_msg = 'Scraped data must be of dictionary type'
    assert str(exc_info.value) == expected_msg


# ==== Тесты для PageNumberValidator ====

def test_page_number_validator_for_correct_value() -> None:
    """ Тест валидации корректного номера страницы """
    page_value = 9
    assert PageNumberValidator.validate(page_value) == page_value


def test_page_number_validator_for_overflow_value() -> None:
    """ Тест валидации номера страницы, выходящего за допустимые границы """
    page_value = 100_000_000
    with pytest.raises(ValueError) as exc_info:
        PageNumberValidator.validate(page_value)
    expected_msg = 'The number of pages must be between 0 and 100,000 (exclusive)'
    assert str(exc_info.value) == expected_msg


def test_page_number_validator_for_invalid_value_type() -> None:
    """ Тест валидации номера страницы с некорректным типом значения """
    page_value: Any = '9'
    with pytest.raises(TypeError) as exc_info:
        PageNumberValidator.validate(page_value)
    expected_msg = 'Number of pages must be an integer value'
    assert str(exc_info.value) == expected_msg
