from datetime import datetime
temp_created_date = datetime.today()

#Запрос информации
username = input("Введите имя пользователя: ")
title = input("Заголовок: \n")
content = input("Введите описание заметки: \n")
status = input("Введите статус заметки (например, 'Активна', 'Выполнена'): ")

created_date = datetime.strftime(temp_created_date, "%d.%m")

temp_issue_date = input("Дата дэдлайна в формате дд.мм.гггг - ")
formatted_issue_date = datetime.strptime(temp_issue_date, "%d.%m.%Y").strftime("%d.%m")

#Вывод данных
print("\nВы ввели следующие данные:")
print("Имя пользователя:", username)
print("Заголовок заметки:", title)
print("Описание заметки:", content)
print("Статус заметки:", status)
print("Дата создания заметки:", created_date)
print("Дата истечения заметки:", formatted_issue_date)
