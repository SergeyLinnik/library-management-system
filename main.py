# Словарь library: ключ — название книги, значение — словарь с информацией о книге
library = {
    "Преступление и наказание": {
        "author": "Фёдор Достоевский",
        "year": 1866,
        "available": True
    },
    "Мастер и Маргарита": {
        "author": "Михаил Булгаков",
        "year": 1967,
        "available": False
    },
    "Война и мир": {
        "author": "Лев Толстой",
        "year": 1869,
        "available": True
    }
}

# Функция для отображения списка всех книг
def book_list_view(library):
    if not library:
        print("В библиотеке пока нет книг.")
        return

    print("Список книг в библиотеке:")
    for title in library:
        print(f"- {title}")

# Вызов функции для проверки
book_list_view(library)

# Проверка случая с пустой библиотекой
empty_library = {}
book_list_view(empty_library)
