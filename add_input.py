from datetime import datetime
temp_created_date = datetime.today()

# Запрашиваем у пользователя информацию
username = input("Введите имя пользователя: ")
content = input("Введите описание заметки: \n")
status = input("Введите статус заметки (например, 'Активна', 'Выполнена'): ")

created_date = datetime.strftime(temp_created_date, "%d.%m")

temp_issue_date = input("Дата дэдлайна в формате дд.мм.гггг - ")
formatted_issue_date = datetime.strptime(temp_issue_date, "%d.%m.%Y").strftime("%d.%m")



# Запрашиваем несколько заголовков и добавляем их в список
title1 = input("Введите первый заголовок заметки: ")
title2 = input("Введите второй заголовок заметки: ")
title3 = input("Введите третий заголовок заметки: ")
titles = [title1, title2, title3]


# Выводим все данные
print("\nВы ввели следующие данные:")
print("Имя пользователя:", username)
print("Заголовки заметки:", titles)
print("Описание заметки:", content)
print("Статус заметки:", status)
print("Дата создания заметки:", created_date)
print("Дата истечения заметки:", formatted_issue_date)
