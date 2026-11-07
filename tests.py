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
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    
    def test_set_book_genre_from_list_genre(self):
        
        collector = BooksCollector()
        collector.add_new_book('Этюд в багровых тонах')
        collector.set_book_genre('Этюд в багровых тонах', 'Детективы')
        
        assert collector.get_book_genre('Этюд в багровых тонах') == 'Детективы'
    
    @pytest.mark.parametrize('not_exist_genre', ['Фэнтези', 'Роман', ''])    
    def test_set_book_genre_not_exist_in_list_genre(self, not_exist_genre):
             
        collector = BooksCollector()
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', not_exist_genre)
        
        assert collector.get_book_genre('Гарри Поттер') == ''       
        
    def test_get_book_genre_existing_book_returns_genre(self):
        
        collector = BooksCollector()
        collector.add_new_book('Этюд в багровых тонах')
        collector.set_book_genre('Этюд в багровых тонах', 'Детективы')
        
        assert collector.get_book_genre('Этюд в багровых тонах') == 'Детективы'
        
    def test_get_books_with_specific_genre_checking_not_existing_genre(self):
        
        collector = BooksCollector()
        collector.add_new_book('Этюд в багровых тонах')
        collector.set_book_genre('Этюд в багровых тонах', 'Детективы')
        
        assert collector.get_books_with_specific_genre('Роман') == []
    
    def test_get_books_with_specific_genre_checking_existing_genre(self):
            
        collector = BooksCollector()
        collector.add_new_book('Этюд в багровых тонах')
        collector.add_new_book('Кэрри')
        collector.set_book_genre('Этюд в багровых тонах', 'Детективы')
        collector.set_book_genre('Кэрри', 'Ужасы')
        
        assert collector.get_books_with_specific_genre('Ужасы') == ['Кэрри']
        
    def test_get_books_genre_contains_two_books(self):
        
        collector = BooksCollector()
        collector.add_new_book('Этюд в багровых тонах')
        collector.add_new_book('Кэрри')
        
        assert len(collector.get_books_genre()) == 2
        
    def test_get_books_for_children_includes_children_books(self):
        
        collector = BooksCollector()
        collector.add_new_book('Приключения Электроника')
        collector.set_book_genre('Приключения Электроника', 'Фантастика')
        
        assert 'Приключения Электроника' in collector.get_books_for_children()
        
    @pytest.mark.parametrize('adult_genre', ['Ужасы', 'Детективы'])   
    def test_get_books_for_children_excludes_adult_books(self, adult_genre):
        
        collector = BooksCollector()
        collector.add_new_book('Взрослая книга')
        collector.set_book_genre('Взрослая книга', adult_genre)
        
        assert 'Взрослая книга' not in collector.get_books_for_children()
        
    def test_add_book_in_favorites_adding_book(self):
        
        collector = BooksCollector()
        collector.add_new_book('Кэрри')
        collector.add_book_in_favorites('Кэрри')
        
        assert 'Кэрри' in collector.get_list_of_favorites_books()
        
    def test_add_book_in_favorites_book_not_in_books_genre(self):
    
       collector = BooksCollector()
       collector.add_book_in_favorites('Гарри Поттер')
       
       assert 'Гарри Поттер' not in collector.get_list_of_favorites_books()    

    def test_delete_book_from_favorites_deleting_book(self):
        
        collector = BooksCollector()
        collector.add_new_book('Кэрри')
        collector.add_book_in_favorites('Кэрри')
        collector.delete_book_from_favorites('Кэрри')
        
        assert 'Кэрри' not in collector.get_list_of_favorites_books()
        
    def test_delete_book_from_favorites_not_in_favorites(self):
        
        collector = BooksCollector()
        collector.add_new_book('Кэрри')
        collector.delete_book_from_favorites('Кэрри')
        
        assert collector.get_list_of_favorites_books() == []
    
    def test_get_list_of_favorites_books_contains_two_books(self):
        
        collector = BooksCollector()
        collector.add_new_book('Кэрри')
        collector.add_new_book('Этюд в багровых тонах')        
        collector.add_book_in_favorites('Кэрри')    
        collector.add_book_in_favorites('Этюд в багровых тонах')
        
        assert len(collector.get_list_of_favorites_books()) == 2