Интсрукция по разворачиванию приложения:
1. Склонируйте репозиторий по ссылке https://github.com/Badmfk/users_polls_api.
2. Создайте и войдите в вирутальное окружение.
3. Установите зависимости:
    - pip install -r requirements.txt
4. Создайте миграции.
    - python manage.py makemigrations
5. Создайте таблицы.
    - python manage.py migrate
5. Создайте суперпользователя.
    - python manage.py createsuperuser
6. Запустите сервер.
    - python manage.py runserver
7. Зайдите на панель администратора по ссылке '/admin/' для добавления/удаления/редактирования опросов, вопросов и вариантов ответа.
8. Для создания анонимного пользователя нужно отправить POST запрос по ссылке '/api/user/' с параметрами:
{
	"user":
	{
		"name": str
	}
}
9. Для получения всех опросов нужно отправить GET запрос по ссылке '/api/polls/.
10. Для получения списка вопросов в опросе нужно отправить GET запрос по ссылке '/api/poll/<int:poll_id>/'.
11. Для прохождения опроса нужно отправить POST запрос по ссылке '/api/answer/' с параметрами:
{
	"answer":
	{
		"name_id": int,
		"question_id": int,
		"own_text": str,
		"one_choice_id": int,
		"several_choice": list,
		"poll_id": int
	}
}
12. Для получения результатов опроса нужно отправить GET запрос по ссылке'/api/get_answers/<int:name_id>/<int:poll_id>'.

    
