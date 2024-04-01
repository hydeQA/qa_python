import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    def test_set_book_genre(self, collector):
        collector.add_new_book('Бойцовский клуб')
        collector.set_book_genre('Бойцовский клуб', 'Фантастика')

        assert collector.get_book_genre('Бойцовский клуб') == 'Фантастика'

    def test_get_book_genre(self, collector):
        collector.add_new_book('Молчание ягнят')
        collector.set_book_genre('Молчание ягнят', 'Ужасы')

        assert collector.get_book_genre('Молчание ягнят') == 'Ужасы'

    @pytest.mark.parametrize("genre, expected_books", [
        ('Фантастика', ['Бойцовский клуб', 'Дюна']),
        ('Ужасы', ['Молчание ягнят']),
        ('Роман', [])
    ])
    def test_get_books_with_specific_genre(self, collector, genre, expected_books):
        collector.add_new_book('Бойцовский клуб')
        collector.add_new_book('Молчание ягнят')
        collector.add_new_book('Дюна')
        collector.set_book_genre('Бойцовский клуб', 'Фантастика')
        collector.set_book_genre('Молчание ягнят', 'Ужасы')
        collector.set_book_genre('Дюна', 'Фантастика')
        actual_books = collector.get_books_with_specific_genre(genre)

        assert actual_books == expected_books

    def test_get_books_genre(self, collector):
        collector.add_new_book('Бойцовский клуб')
        collector.add_new_book('Молчание ягнят')
        collector.add_new_book('Дюна')
        collector.set_book_genre('Бойцовский клуб', 'Фантастика')
        collector.set_book_genre('Молчание ягнят', 'Ужасы')
        collector.set_book_genre('Дюна', 'Фантастика')

        assert collector.get_books_genre() == {'Бойцовский клуб': 'Фантастика', 'Молчание ягнят': 'Ужасы',
                                         'Дюна': 'Фантастика'}


    def test_get_books_for_children(self, collector):
        collector.add_new_book('Дюна')
        collector.add_new_book('Рататуй')
        collector.set_book_genre('Дюна', 'Ужасы')
        collector.set_book_genre('Рататуй', 'Мультфильмы')
        children_books = collector.get_books_for_children()
        expected_books = ['Рататуй']

        assert children_books == expected_books

    def test_add_book_in_favorites(self, collector):
        collector.add_new_book('Дюна')
        collector.add_new_book('Рататуй')
        collector.add_book_in_favorites('Рататуй')
        collector.add_book_in_favorites('Дюна')

        assert collector.get_list_of_favorites_books() == ['Рататуй', 'Дюна']

    def test_delete_book_in_favorites(self, collector):
        collector.add_new_book('Дюна')
        collector.add_new_book('Рататуй')
        collector.add_book_in_favorites('Рататуй')
        collector.add_book_in_favorites('Дюна')

        collector.delete_book_from_favorites('Рататуй')

        assert collector.get_list_of_favorites_books() == ['Дюна']

