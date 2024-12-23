from datetime import datetime
temp_created_date = datetime.today()

note = {}

# Запрашиваем имя пользователя
note["username"] = input("Введите имя пользователя: ")
# Создаем список заголовков заметки
note["titles"] = []
while True:
    title = input(f"Введите заголовок заметки(или оставьте пустым для завершения, или напиши стоп): ")
    if title == "" or title.lower() == "стоп":
        break

    if title not in note["titles"]:
        note["titles"].append(title)
    elif title in note["titles"]:
        print("Такой заголовок уже добавлен, введите другой")


# Запрашиваем остальные данные
note["content"] = input("Введите описание заметки: \n")
note["status"] = input("Введите статус заметки (например, 'Активна', 'Выполнена'): ")

note["created_date"] = datetime.strftime(temp_created_date, "%d.%m")
# Форматирование даты
temp_issue_date = input("Дата дэдлайна в формате дд.мм.гггг - ")
note["formatted_issue_date"] = datetime.strptime(temp_issue_date, "%d.%m.%Y").strftime("%d.%m")





# Выводим собранные данные
print("\nСобранная информация о заметке:")
for key, value in note.items():
    print(f"{key.capitalize()}: {value}")
