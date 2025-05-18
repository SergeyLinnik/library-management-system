def add_book(library, title, author, year):
    """
    Добавляет или обновляет информацию о книге в библиотеке.
    
    :param library: словарь библиотеки
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
    return library


def remove_book(library, title):
    """
    Удаляет книгу из библиотеки по её названию.
    
    :param library: словарь библиотеки
    :param title: Название книги
    """
    if title in library:
        del library[title]
        print(f"Книга '{title}' успешно удалена из библиотеки.\n")
    else:
        print(f"Книга '{title}' не найдена в библиотеке.\n")
    return library


def issue_book(library, title):
    """
    Отмечает книгу как выданную (available = False).
    
    :param library: словарь библиотеки
    :param title: Название книги
    """
    if title in library:
        if library[title]["available"] is not False:
            library[title]["available"] = False
            print(f"Книга '{title}' успешно выдана.\n")
        else:
            print(f"Книга '{title}' уже выдана.\n")
    else:
        print(f"Книга '{title}' не найдена в библиотеке.\n")
    return library


def return_book(library, title):
    """
    Отмечает книгу как возвращённую (available = True).
    
    :param library: словарь библиотеки
    :param title: Название книги
    """
    if title in library:
        if library[title]["available"] is not True:
            library[title]["available"] = True
            print(f"Книга '{title}' успешно возвращена в библиотеку.\n")
        else:
            print(f"Книга '{title}' уже находится в библиотеке.\n")
    else:
        print(f"Книга '{title}' не найдена в библиотеке.\n")
    return library


def book_list_view(library):
    """
    Выводит список всех книг в библиотеке с их статусом.
    """
    if not library:
        print("В библиотеке пока нет книг.")
        return

    print("\n=== Список книг в библиотеке ===")
    for title, info in library.items():
        status = "в наличии"
        if info["available"] is False:
            status = "выдана"
        elif info["available"] is None:
            status = "статус не определён"
        print(f"- {title} ({info['author']}, {info['year']}) — статус: {status}")
    print()


def find_book(library, title):
    """
    Выводит информацию о книге по её названию.
    """
    if title in library:
        info = library[title]
        print(f"\nИнформация о книге '{title}':")
        print(f"Автор: {info['author']}")
        print(f"Год издания: {info['year']}")

        availability = info['available']
        if availability is True:
            print("Статус: Книга доступна")
        elif availability is False:
            print("Статус: Книга выдана")
        else:
            print("Статус: Книга в библиотеке, но её статус не определён")

        print()
    else:
        print(f"\nКнига '{title}' не найдена в библиотеке.\n")


# ========================
# Пользовательское меню
# ========================

def show_menu():
    print("📚 Меню управления библиотекой:")
    print("1. Добавить книгу")
    print("2. Удалить книгу")
    print("3. Выдать книгу")
    print("4. Вернуть книгу")
    print("5. Показать все книги")
    print("6. Найти книгу по названию")
    print("7. Выход")


def get_user_choice():
    return input("Выберите действие (1-7): ").strip()


def main():
    library = {}  # Теперь это локальная переменная
    while True:
        show_menu()
        choice = get_user_choice()

        if choice == "1":
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            try:
                year = int(input("Введите год издания книги: "))
            except ValueError:
                print("Ошибка: год должен быть числом.\n")
                continue
            add_book(library, title, author, year)

        elif choice == "2":
            title = input("Введите название книги для удаления: ")
            remove_book(library, title)

        elif choice == "3":
            title = input("Введите название книги для выдачи: ")
            issue_book(library, title)

        elif choice == "4":
            title = input("Введите название книги для возврата: ")
            return_book(library, title)

        elif choice == "5":
            book_list_view(library)

        elif choice == "6":
            title = input("Введите название книги для поиска: ")
            find_book(library, title)

        elif choice == "7":
            print("Завершение работы программы.")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")

# Запуск программы
if __name__ == "__main__":
    main()
