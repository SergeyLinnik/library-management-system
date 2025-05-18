# Словарь library: ключ — название книги, значение — словарь с информацией о книге
library = {}

def add_book(title, author, year):
    """
    Добавляет или обновляет информацию о книге в библиотеке.
    
    :param title: Название книги
    :param author: Автор книги
    :param year: Год издания
    """
    if title in library:
        print(f"Книга '{title}' уже существует в библиотеке. Хотите обновить информацию?")
        choice = input("Введите 'да' для обновления, любую другую клавишу для отмены: ").strip().lower()
        if choice == 'да':
            library[title] = {
                "author": author,
                "year": year,
                "available": None
            }
            print(f"Информация о книге '{title}' успешно обновлена.\n")
    else:
        library[title] = {
            "author": author,
            "year": year,
            "available": None
        }
        print(f"Книга '{title}' успешно добавлена в библиотеку.\n")


def remove_book(title):
    """
    Удаляет книгу из библиотеки по её названию.
    
    :param title: Название книги
    """
    if title in library:
        del library[title]
        print(f"Книга '{title}' успешно удалена из библиотеки.\n")
    else:
        print(f"Книга '{title}' не найдена в библиотеке.\n")


def book_list_view(library):
    """
    Выводит список всех книг в библиотеке.
    """
    if not library:
        print("В библиотеке пока нет книг.")
        return

    print("Список книг в библиотеке:")
    for title in library:
        print(f"- {title}")
    print()


# === Пример использования ===

# Добавляем несколько книг
add_book("Преступление и наказание", "Фёдор Достоевский", 1866)
add_book("Мастер и Маргарита", "Михаил Булгаков", 1967)

# Выводим список всех книг
book_list_view(library)

# Попытка удалить книгу
remove_book("Преступление и наказание")

# Попытка удалить несуществующую книгу
remove_book("Не существующая книга")

# Выводим обновлённый список
book_list_view(library)
