# Створюємо пусту множину для зберігання унікальних слів
new_words = set()

# Функція для додавання нового слова до словника
def add_word(word):
    word = word.strip().lower()  # Прибираємо пробіли та переводимо в нижній регістр
    new_words.add(word)          # Додаємо слово до множини (автоматично уникає повторів)

# Функція для пошуку слів за першими літерами
def find_words_by_prefix(prefix):
    prefix = prefix.lower()  # Переводимо префікс до нижнього регістру для порівняння
    # Генератор списку для фільтрації слів, що починаються на prefix
    result = [word for word in new_words if word.startswith(prefix)]
    return sorted(result)  # Повертаємо список у відсортованому порядку

# Функція для підрахунку кількості унікальних слів
def count_words():
    return len(new_words)

# Основна частина програми
while True:
    print("\n=== Словник нових слів ===")
    print("1. Додати нове слово")
    print("2. Знайти слова за початковими літерами")
    print("3. Показати кількість унікальних слів")
    print("4. Показати всі слова")
    print("5. Вийти")

    choice = input("Оберіть дію (1-5): ")

    if choice == "1":
        word = input("Введіть нове слово: ")
        add_word(word)
        print("Слово додано!")
    elif choice == "2":
        prefix = input("Введіть початок слова: ")
        matched = find_words_by_prefix(prefix)
        if matched:
            print("Знайдені слова:", ", ".join(matched))
        else:
            print("Слів з таким початком не знайдено.")
    elif choice == "3":
        print(f"У словнику {count_words()} унікальних слів.")
    elif choice == "4":
        print("Усі слова у словнику:")
        for word in sorted(new_words):
            print("-", word)
    elif choice == "5":
        print("Вихід з програми. До побачення!")
        break
    else:
        print("Невірний вибір. Спробуйте ще раз.")
