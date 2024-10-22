import wikipediaapi

# Инициализация Wikipedia API
wiki = wikipediaapi.Wikipedia('ru')

def get_related_pages(page):
    """Получение списка связанных страниц."""
    links = page.links
    related_pages = list(links.keys())
    return related_pages

def display_paragraphs(page):
    """Отображение параграфов статьи."""
    paragraphs = page.text.split('\n')
    for i, paragraph in enumerate(paragraphs):
        if paragraph.strip():
            print(f"\n--- Параграф {i + 1} ---")
            print(paragraph)

def choose_related_page(related_pages):
    """Предложение выбора из связанных страниц."""
    for i, title in enumerate(related_pages[:10], 1):  # Отображаем только первые 10 статей
        print(f"{i}. {title}")
    try:
        choice = int(input("\nВыберите номер страницы для перехода (или 0 для возврата): "))
        if 1 <= choice <= len(related_pages[:10]):
            return related_pages[choice - 1]
        else:
            return None
    except ValueError:
        return None

def main():
    query = input("Введите запрос для поиска на Википедии: ")
    page = wiki.page(query)

    if not page.exists():
        print("Статья не найдена!")
        return

    while True:
        print(f"\n--- Статья: {page.title} ---")
        print(f"Ссылка: {page.fullurl}")
        print("\nВыберите действие:")
        print("1. Листать параграфы статьи")
        print("2. Перейти на связанную статью")
        print("3. Выйти из программы")

        action = input("Введите номер действия: ")

        if action == '1':
            display_paragraphs(page)
        elif action == '2':
            related_pages = get_related_pages(page)
            if related_pages:
                selected_title = choose_related_page(related_pages)
                if selected_title:
                    page = wiki.page(selected_title)
                else:
                    print("Неверный выбор или возврат.")
            else:
                print("Нет связанных страниц.")
        elif action == '3':
            print("Выход из программы.")
            break
        else:
            print("Неверный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main()

