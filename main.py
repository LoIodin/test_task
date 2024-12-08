import json
import os
import pprint


def add_book(title: str, author: str, year: int):
    try:
        with open('library.json', 'r', encoding='utf-8') as f:
            books = json.load(f)

        if books['books']:
            id_book = books['books'][-1]['id']
        else:
            id_book = 0

        book = {
            'id': id_book + 1,
            'title': title,
            'author': author,
            'year': year,
            'status': 'В наличии'
        }
        books['books'].append(book)

        with open('library.json', 'w', encoding='utf-8') as f:
            json.dump(books, f, indent=4, ensure_ascii=False)
        return print('Книга добавлена!')
    except FileNotFoundError:
        with open('library.json', 'w', encoding='utf-8') as f:
            books = {
                'books': [
                    {
                        'id': 1,
                        'title': title,
                        'author': author,
                        'year': year,
                        'status': 'В наличии'
                    }
                ]
            }
            json.dump(books, f, indent=4, ensure_ascii=False)
        return print('Книга добавлена!')


def delete_book(id_book: int):
    with open('library.json', encoding='utf-8') as f:
        books = json.load(f)

    for book in books['books']:
        if book['id'] == id_book:
            books['books'].remove(book)
            with open('library.json', 'w', encoding='utf-8') as f:
                json.dump(books, f, indent=4, ensure_ascii=False)
            return print('Книга удалена')

    return print('Книги с таким ID не существует')


def search_book(title: str = None, author: str = None, year: int = None):
    with open('library.json', encoding='utf-8') as f:
        books = json.load(f)

    result = {}
    for book in books['books']:
        if book['title'] == title or book['author'] == author or book['year'] == year:
            result = book
            pprint.pprint(result)
    if not result:
        print('Такой книги не найдено')


def show_books():
    with open('library.json', encoding='utf-8') as f:
        books = json.load(f)
    for book in books['books']:
        pprint.pprint(book)
        print()


def change_status(id_book: int, status: str):
    if status not in ['В наличии', 'Выдана']:
        return print('Статус должен быть либо "В наличии", либо "Выдана"')
    with open('library.json', encoding='utf-8') as f:
        books = json.load(f)

    for book in books['books']:
        if book['id'] == id_book:
            book['status'] = status
            with open('library.json', 'w', encoding='utf-8') as f:
                json.dump(books, f, indent=4, ensure_ascii=False)
            return print('Статус книги изменен')

    return print('Книги с таким ID не существует')


while True:
    os.system('cls||clear')
    print("""Добро пожаловать в программу для управления библиотекой книг!
Выберите номер одной из доступных функций:
1. Добавление книги
2. Удаление книги
3. Поиск книги
4. Отображение всех книг
5. Изменение статуса книги
6. Выйти из программы
    """)
    try:
        number_func = int(input('Введите номер функции: '))
        match number_func:
            case 1:
                try:
                    print('Для добавления книги нужно ввести название, автора и год издания')
                    title_book = input('Введите название книги: ')
                    author_book = input('Введите автора книги: ')
                    year_book = int(input('Введите год издания книги: '))
                    add_book(title_book, author_book, year_book)
                    input('Для продолжения нажмите любую кнопку...')
                except ValueError:
                    print('Пожалуйста, введите число в строку года!')
                    input('Для продолжения нажмите любую кнопку...')
            case 2:
                print('Для удаления книги нужно ввести ее ID')
                id_delete = int(input('Введите ID книги: '))
                delete_book(id_delete)
                input('Для продолжения нажмите любую кнопку...')
            case 3:
                print('''Для поиска книги нужно ввести название, автора или год издания книги.
Выберите способ поиска
1. Поиск по названию
2. Поиск по автору
3. Поиск по дате издания
                ''')
                try:
                    choice_of_search = int(input('Выберите способ поиска: '))
                    match choice_of_search:
                        case 1:
                            title_book = input('Введите название книги: ')
                            search_book(title=title_book)
                            input('Для продолжения нажмите любую кнопку...')
                        case 2:
                            author_book = input('Введите автора книги: ')
                            search_book(author=author_book)
                            input('Для продолжения нажмите любую кнопку...')
                        case 3:
                            try:
                                year_book = int(input('Введите год издания книги: '))
                                search_book(year=year_book)
                                input('Для продолжения нажмите любую кнопку...')
                            except ValueError:
                                print('Пожалуйста, введите год издания!')
                                input('Для продолжения нажмите любую кнопку...')
                        case _:
                            print('Такой команды нет, попробуйте еще')
                            input('Для продолжения нажмите любую кнопку...')
                except ValueError:
                    print('Пожалуйста, введите номер функции')
                    input('Для продолжения нажмите любую кнопку...')
            case 4:
                show_books()
                input('Для продолжения нажмите любую кнопку...')
            case 5:
                try:
                    print('Для изменения статуса книги нужно ввести ее ID и новый статус')
                    id_change = int(input('Введите ID книги: '))
                    new_status = input('Введите новый статус книги [В наличии/Выдана]: ')
                    change_status(id_change, new_status)
                    input('Для продолжения нажмите любую кнопку...')
                except ValueError:
                    print('Пожалуйста, введите номер ID!')
                    input('Для продолжения нажмите любую кнопку...')
            case 6:
                print('До свидания!')
                break
            case _:
                print('Такой команды нет, попробуйте еще')
                input('Для продолжения нажмите любую кнопку...')
    except ValueError:
        print('Пожалуйста, введите номер функции')
        input('Для продолжения нажмите любую кнопку...')
