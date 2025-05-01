import pytest
from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()


class TestBooksCollector:
    @pytest.fixture
    def collector(self):
        return BooksCollector()

    @pytest.mark.parametrize('name, expected, is_duplicate', [
        ('Книга 1', True, False),
        ('A' * 40, True, False),
        ('', False, False),
        ('A' * 41, False, False),
        ('Книга 1', False, True)
    ])
    def test_add_new_book(self, collector, name, expected, is_duplicate):
        if is_duplicate:
            collector.add_new_book(name)

        initial_count = len(collector.books_genre)
        collector.add_new_book(name)
        new_count = len(collector.books_genre)

        if expected:
            assert new_count == initial_count + 1
            assert name in collector.books_genre
        else:
            if name == 'Книга 1' and is_duplicate:
                assert new_count == initial_count
            else:
                assert name not in collector.books_genre

    def test_get_book_genre_with_genre(self, collector):
        collector.add_new_book('Книга 1')
        collector.set_book_genre('Книга 1', 'Фантастика')
        assert collector.get_book_genre('Книга 1') == 'Фантастика'

    def test_get_book_genre_without_genre(self, collector):
        collector.add_new_book('Книга без жанра')
        assert collector.get_book_genre('Книга без жанра') == ''

    def test_set_book_genre_valid(self, collector):
        collector.add_new_book('Книга 1')
        collector.set_book_genre('Книга 1', 'Фантастика')
        assert collector.get_book_genre('Книга 1') == 'Фантастика'

    def test_set_book_genre_invalid(self, collector):
        collector.add_new_book('Книга 1')
        collector.set_book_genre('Книга 1', 'Несуществующий жанр')
        assert collector.get_book_genre('Книга 1') == ''

    def test_get_books_with_specific_genre(self, collector):
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        collector.set_book_genre('Книга 1', 'Фантастика')
        collector.set_book_genre('Книга 2', 'Ужасы')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Книга 1']

    def test_get_books_for_children(self, collector):
        collector.add_new_book('Детская книга')
        collector.add_new_book('Взрослая книга')
        collector.set_book_genre('Детская книга', 'Мультфильмы')
        collector.set_book_genre('Взрослая книга', 'Ужасы')
        assert collector.get_books_for_children() == ['Детская книга']

    def test_add_book_in_favorites(self, collector):
        collector.add_new_book('Книга 1')
        collector.add_book_in_favorites('Книга 1')
        assert 'Книга 1' in collector.favorites

    def test_add_book_in_favorites_twice(self, collector):
        collector.add_new_book('Книга 1')
        collector.add_book_in_favorites('Книга 1')
        collector.add_book_in_favorites('Книга 1')
        assert len(collector.favorites) == 1

    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book('Книга 1')
        collector.add_book_in_favorites('Книга 1')
        collector.delete_book_from_favorites('Книга 1')
        assert 'Книга 1' not in collector.favorites

    def test_get_list_of_favorites_books(self, collector):
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        collector.add_book_in_favorites('Книга 1')
        assert collector.get_list_of_favorites_books() == ['Книга 1']