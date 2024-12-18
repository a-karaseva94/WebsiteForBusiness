# Реализация серверной части сайта (backend) для бизнеса на примере финансового аналитика

Проект решает задачу по разработке сервисной части сайта для ведения бизнеса. В данном случае сайт сделан для действующего финансового аналитика.

Работа бэкенда не видна пользователю, но именно он помогает сделать так, чтобы сервисы понимали запросы пользователей и корректно реагировали на их действия.


## Использование
Для того, чтобы использовать проект:
1. Скачайте проект с GitHub;
2. Создайте виртуальное окружение: в Terminal можно воспользоваться командой «python -m venv venv»;
3. Установите все пакеты и их версии, необходимые для работы проекта, через файл зависимостей : в Terminal можно воспользоваться командой «pip install -r requirements.txt».  

Можно приступать к работе!


## Демонстрация работы (структура сайта)
Сайт включает следующие страницы:
1. Главная страница.
   
   На странице расположены стилизованные кнопки с переходами по другим страницам сайта. Доступ к главной странице открыт всем.
   
   ![Илюстрация к проекту 1](https://github.com/a-karaseva94/WebsiteForBusiness/blob/master/screenshorts%20работы%20сайта/Главная%20страница.png)
   
2. О нас.
   
   На странице расположена общая информация о компании и услугах. Есть ссылки на другие сайты и общее меню (такое же, как на главной странице, но справа).
   Доступ к странице открыт всем.
   
   ![Илюстрация к проекту 2](https://github.com/a-karaseva94/WebsiteForBusiness/blob/master/screenshorts%20работы%20сайта/О%20нас.png)
   
   ![Илюстрация к проекту 3](https://github.com/a-karaseva94/WebsiteForBusiness/blob/master/screenshorts%20работы%20сайта/Переход%20на%20сайт%20ФРП%20со%20страницы%20О%20нас.png)

   ![Илюстрация к проекту 4](https://github.com/a-karaseva94/WebsiteForBusiness/blob/master/screenshorts%20работы%20сайта/Переход%20на%20сайт%20РФРП%20со%20страницы%20О%20нас.png)
   
3. Услуги.
   
   На странице в виде таблицы представлены оказываемые услуги (реализован пагинатор для перехода по страницам, а также механизм выбора количества элементов на странице - 2 или 5). Просмотр таблицы открыт всем пользователям, однако - напротив услуг в таблице есть кнопки "Добавить в корзину". Данные кнопки работают только для авторизованных пользователей, при нажатии неавторизованным пользователем он будет перекинут на страницу "Вход".
   
   Войти или зарегистрироваться также можно на этой странице, как и выйти потом.
   
   Есть общее меню (такое же, как на главной странице, но справа).

   ![Илюстрация к проекту 5](https://github.com/a-karaseva94/WebsiteForBusiness/blob/master/screenshorts%20работы%20сайта/Услуги%20(без%20авторизации).png)
   
   ![Илюстрация к проекту 6](https://github.com/a-karaseva94/WebsiteForBusiness/blob/master/screenshorts%20работы%20сайта/Услуги%20(с%20авторизацией).png)
   
4. Корзина.
   
   Корзина доступна только авторизованным пользователям. При попытке перехода в Корзину неавторизованный пользователь будет перекинут на страницу "Вход".
   
   После входа пользователь может:
   - увеличивать/уменьшать количество товаров в Корзине,
   - продолжать покупки - реализована ссылка на страницу Услуги,
   - оформлять заказ - реализована ссылка на страницу разработчика в телеграме (в перспективе возможно доработать и отправлять заказ на почту или в телеграм-бот).
     
   Есть общее меню (такое же, как на главной странице, но справа).

   ![Илюстрация к проекту 7](https://github.com/a-karaseva94/WebsiteForBusiness/blob/master/screenshorts%20работы%20сайта/Корзина%20(открывается%20при%20авторизации).png)

   ![Илюстрация к проекту 8](https://github.com/a-karaseva94/WebsiteForBusiness/blob/master/screenshorts%20работы%20сайта/Корзина%20с%20товаром.png)

   ![Илюстрация к проекту 9](https://github.com/a-karaseva94/WebsiteForBusiness/blob/master/screenshorts%20работы%20сайта/Оформление%20из%20корзины.png)

5. Регистрация.
    
   На странице представлена Django-форма для регистрации пользователя. Также в случае, если пользователь передумал, предусмотрен возврат в услугам.

   ![Илюстрация к проекту 10](https://github.com/a-karaseva94/WebsiteForBusiness/blob/master/screenshorts%20работы%20сайта/Регистрация.png)
   
6. Вход.
   
   На странице представлена Django-форма для входа пользователя.
   
   Есть общее меню (такое же, как на главной странице, но справа).

   ![Илюстрация к проекту 11](https://github.com/a-karaseva94/WebsiteForBusiness/blob/master/screenshorts%20работы%20сайта/Вход.png)

   
## Команда проекта
[Карасева Анастасия](https://t.me/karasevaad)


## Источники

Полезные источники:

[Аутентификация в приложениях](https://tproger.ru/articles/kak-nastroit-autentifikaciyu-v-veb-prilozheniyah-na-django)

[Ограничение доступа в приложениях](https://proglib.io/p/django-s-nulya-chast-2-registraciya-avtorizaciya-ogranichenie-dostupa-2022-06-08)

[Функционал корзины](https://www.geeksforgeeks.org/how-to-add-cart-in-a-web-page-using-django/)

[Цвета html](https://colorscheme.ru/html-colors.html)

[Таблица основных тегов html](https://uguide.ru/tablica-osnovnykh-tegov-html-s-primerami)
