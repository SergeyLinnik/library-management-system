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
                "available": None  # Не определено при добавлении
            }
            print(f"Информация о книге '{title}' успешно обновлена.\n")
    else:
        library[title] = {
            "author": author,
            "year": year,
            "available": True  # По умолчанию книга доступна
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


def issue_book(title):
    """
    Отмечает книгу как выданную (available = False).
    
    :param title: Название книги
    """
    if title in library:
        if library[title]["available"] is True or library[title]["available"] is None:
            library[title]["available"] = False
            print(f"Книга '{title}' успешно выдана.\n")
        else:
            print(f"Книга '{title}' уже выдана.\n")
    else:
        print(f"Книга '{title}' не найдена в библиотеке.\n")


def return_book(title):
    """
    Отмечает книгу как возвращённую (available = True).
    
    :param title: Название книги
    """
    if title in library:
        if library[title]["available"] is False or library[title]["available"] is None:
            library[title]["available"] = True
            print(f"Книга '{title}' успешно возвращена в библиотеку.\n")
        else:
            print(f"Книга '{title}' уже находится в библиотеке.\n")
    else:
        print(f"Книга '{title}' не найдена в библиотеке.\n")


def book_list_view(library):
    """
    Выводит список всех книг в библиотеке с их статусом.
    """
    if not library:
        print("В библиотеке пока нет книг.")
        return

    print("=== Список книг в библиотеке ===")
    for title, info in library.items():
        status = "в наличии"
        if info["available"] is False:
            status = "выдана"
        elif info["available"] is None:
            status = "статус не определён"
        print(f"- {title} ({info['author']}, {info['year']}) — статус: {status}")
    print()


def find_book(title):
    """
    Выводит информацию о книге по её названию.
    
    :param title: Название книги
    """
    if title in library:
        info = library[title]
        status = "в наличии"
        if info["available"] is False:
            status = "выдана"
        elif info["available"] is None:
            status = "статус не определён"

        print(f"\nИнформация о книге '{title}':")
        print(f"Автор: {info['author']}")
        print(f"Год издания: {info['year']}")
        print(f"Статус: {status}\n")
    else:
        print(f"\nКнига '{title}' не найдена в библиотеке.\n")


# === Тело программы ===

# Вывод начального состояния библиотеки
book_list_view(library)

# Добавляем несколько книг
add_book("Преступление и наказание", "Фёдор Достоевский", 1866)
add_book("Мастер и Маргарита", "Михаил Булгаков", 1967)

# Выводим список после добавления
book_list_view(library)

# Выдаем одну из книг
issue_book("Преступление и наказание")

# Пытаемся снова выдать эту же книгу
issue_book("Преступление и наказание")

# Возвращаем книгу
return_book("Преступление и наказание")

# Пытаемся снова вернуть эту же книгу
return_book("Преступление и наказание")

# Ищем книгу по названию
find_book("Мастер и Маргарита")
find_book("Неизвестная книга")

# Удаляем книгу
remove_book("Мастер и Маргарита")

# Выводим финальный список
book_list_view(library)

# Пробуем найти удалённую книгу
find_book("Мастер и Маргарита")
