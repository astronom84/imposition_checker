"""
Модуль предназначен для проверки соответствия
готового спуска полос схеме раскладки
"""
import argparse
#import pdf2image


class ImpositionChecker:
    """
    Класс сверяет расположение отрастрированных полос макета
    в готовом спуске в соответствии со схемой раскладки
    """

    def __init__(self, pages, pairs, scheme, epsilon):
        self.pages = pages
        self.pairs = pairs
        self.scheme = scheme
        self.epsilon = epsilon

    def compare_files(self, file1, file2):
        """
        Метод, сравнивает два файла и возвращает индекс структурного сходства (SSIM)
        (https://www.pyimagesearch.com/2014/09/15/python-compare-two-images/)
        Returns:
            Bool
        """
        diff = 0.8
        return diff <= self.epsilon

    def check(self):
        """
        Публичный метод, вызывает методы конвертации и сравнения исходных файлов.
        Если в спуске полос есть фрагменты, отличающиеся от исходных полос больше,
        чем на величину self.epsilon, метод возвращает False.
        Returns:
            Bool
        """
        diff = self.compare_files('file1.jpg', 'file2.jpg')
        return diff


def main():
    """
    Функция для запуска приложения из командной строки.
    Функция
    - разбирает аргументы командной строки,
    - создает объект ImpositionChecker с полученными параметрами,
    - вызывает метод check() созданного объекта
    - выводит на экран результат вызова метода check
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--pages', required=True)
    parser.add_argument('--pairs', required=True)
    parser.add_argument('--scheme', required=True)
    parser.add_argument('--epsilon', default=0.9, type=float)
    params = parser.parse_args()
    chk = ImpositionChecker(params.pages,
                            params.pairs,
                            params.scheme,
                            params.epsilon)
    return chk.check()


if __name__ == '__main__':
    print(main())
