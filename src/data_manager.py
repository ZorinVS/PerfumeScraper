import os

import pandas as pd
from pandas import DataFrame

from src.base import BaseFileManager
from src.utils import OSUtils
from src.validators import GoldAppleDataValidator


class CSVFileManager(BaseFileManager[DataFrame]):
    """ Менеджер для работы с CSV-файлами """

    def save_data(self, scraped_data: dict, filename: str = '') -> None:
        """ Сохранение данных в CSV-файле """
        data = GoldAppleDataValidator.validate(scraped_data)
        filename = OSUtils.generate_filename() if filename == '' else filename
        file_path = self._get_file_path(filename)
        df = pd.DataFrame(data)
        df.to_csv(file_path, encoding='utf-8')

    def load_data(self, filename: str) -> DataFrame:
        """ Выгрузка данных из CSV-файла """
        file_path = self._get_file_path(filename)
        return pd.read_csv(file_path, index_col=0)

    def delete_data(self, filename: str = '') -> None:
        """ Удаление всех файлов или одного конкретного """
        if OSUtils.is_directory_empty(self._dir_path):
            raise FileNotFoundError(f"The directory '{self._dir_path}' is already empty")
        if filename and not OSUtils.is_there_file(filename, self._dir_path):
            raise FileNotFoundError(f"File '{filename}' not found in directory '{self._dir_path}'")

        file_paths = [self._get_file_path(filename)] if filename else [file.path for file in os.scandir(self._dir_path)]
        for path in file_paths:
            os.remove(path)

    def _get_file_path(self, filename: str) -> str:
        """ Получение пути к файлу """
        return os.path.join(self._dir_path, filename)
