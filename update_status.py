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
statuses = ["Выполнена", "В процессе", "Отложено"]
note["status"] = statuses[1]

note["created_date"] = datetime.strftime(temp_created_date, "%d.%m")

# Цикл для проверки правильности ввода даты дэдлайна
while True :
    temp_issue_date = input("Дата дэдлайна в формате дд.мм.гггг - ")
    try:
        note["issue_date"] = datetime.strptime(temp_issue_date, "%d.%m.%Y").strftime("%d.%m") # убираем год
        break  # Выход из цикла, если дата введена правильно

    except ValueError:
    # Если возникает ошибка, значит дата введена неправильно
        print("Вы ввели дату в неверном формате. Пожалуйста, используйте формат дд.мм.гггг.")

# Выводим собранные данные
print("\nСобранная информация о заметке:")
for key, value in note.items():
    print(f"{key.capitalize()}: {value}")

# Цикл для обновления статуса заметки
while True:
        status_new = input("\n Введите статус заметки "
                           "1. Выполнено, 2. В процессе, 3. Отложено или введите свой статус заметки): ")
        #Проверяем на пустую строку
        if status_new == "" :
            print("Вы ввели некорректное значение")
            continue
        # Конвертация ввода в число
        try:
            status_new = int(status_new)
        except ValueError:
            note["status"] = status_new
            break # Выход из цикла после корректного пользовательского ввода

        if status_new == 1:
            note["status"] = statuses [0]
            break
        if status_new == 2:
            note["status"] = statuses [1]
            break
        if status_new == 3:
            note["status"] = statuses [2]
            break
        else:
            print("Вы ввели некорректное значение")

# Выводим новый статус заметки
print(f"Статус заметки успешно обновлён на: {note['status']}")

