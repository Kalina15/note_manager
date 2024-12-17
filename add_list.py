from datetime import datetime
temp_created_date = datetime.today()

# Запрашиваем у пользователя информацию
username = input("Введите имя пользователя: ")
content = input("Введите описание заметки: \n")
status = input("Введите статус заметки (например, 'Активна', 'Выполнена'): ")

created_date = datetime.strftime(temp_created_date, "%d.%m")

temp_issue_date = input("Дата дэдлайна в формате дд.мм.гггг - ")
formatted_issue_date = datetime.strptime(temp_issue_date, "%d.%m.%Y").strftime("%d.%m")


# Создаем список заголовков заметки
titles = []
for i in range(3):
    title = input(f"Введите заголовок заметки {i + 1}: ")
    titles.append(title)



# Выводим все данные
print("\nВы ввели следующие данные:")
print("Имя пользователя:", username)
print("Заголовки заметки:", titles)
print("Описание заметки:", content)
print("Статус заметки:", status)
print("Дата создания заметки:", created_date)
print("Дата истечения заметки:", formatted_issue_date)
