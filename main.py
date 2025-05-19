def add_book(library, title, author, year):
    """Добавляет или обновляет информацию о книге в библиотеке."""
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
            "available": True
        }
        print(f"Книга '{title}' успешно добавлена в библиотеку.\n")
    return library


def remove_book(library, title):
    """Удаляет книгу из библиотеки по её названию."""
    if title in library:
        del library[title]
        print(f"Книга '{title}' успешно удалена из библиотеки.\n")
    else:
        print(f"Книга '{title}' не найдена в библиотеке.\n")
    return library


def issue_book(library, title):
    """Отмечает книгу как выданную (available = False)."""
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
    """Отмечает книгу как возвращённую (available = True)."""
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
    """Выводит список всех книг в библиотеке с их статусом."""
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
    """Выводит информацию о книге по её названию."""
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
# Пользовательское меню через словарь
# ========================

def show_menu():
    print("\n📚 Меню управления библиотекой:")
    print("1. Добавить книгу")
    print("2. Удалить книгу")
    print("3. Выдать книгу")
    print("4. Вернуть книгу")
    print("5. Показать все книги")
    print("6. Найти книгу")
    print("7. Выйти")


def get_user_choice():
    return input("Выберите действие (1-7): ").strip()


def main():
    library = {}

    menu_actions = {
        "1": lambda: add_book(library,
                              input("Введите название книги: "),
                              input("Введите автора книги: "),
                              int(input("Введите год издания: "))),

        "2": lambda: remove_book(library, input("Введите название книги для удаления: ")),
        "3": lambda: issue_book(library, input("Введите название книги для выдачи: ")),
        "4": lambda: return_book(library, input("Введите название книги для возврата: ")),
        "5": lambda: book_list_view(library),
        "6": lambda: find_book(library, input("Введите название книги для поиска: ")),
        "7": lambda: exit(print("Завершение работы программы."))
    }

    while True:
        show_menu()
        choice = get_user_choice()

        action = menu_actions.get(choice)
        if action:
            try:
                action()
            except Exception as e:
                print(f"Ошибка ввода: {e}. Попробуйте снова.")
        else:
            print("Неверный выбор. Попробуйте снова.")


# Запуск программы
if __name__ == "__main__":
    main()
