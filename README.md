# **Parser Python Pep - парсер документов PEP**

### Оглавление
<ol>
 <li><a href="#description">Описание проекта</a></li>
 <li><a href="#stack">Используемые технологии</a></li>
 <li><a href="#start_project">Как развернуть проект?</a></li>
 <li><a href="#required_arg">Аргументы(обязательные)</a></li>
 <li><a href="#arg">Аргументы(опциональные)</a></li>
 <li><a href="#cmd">Примеры команд</a></li>
 <li><a href="#author">Авторы проекта</a></li>
</ol>

___
### Описание проекта:<a name="description"></a>
Парсер собирает статистику по документам PEP, записывает в файл или выводит
на экран, дополнительно реализовано скачивание архива с документацией и
парсинг новостей о версиях Python

___
### **Используемые технологии**<a name="stack"></a>
![](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![](https://img.shields.io/badge/beautiful_soup_4-092E20?style=for-the-badge)
![](https://img.shields.io/badge/HTML-red?style=for-the-badge)
![](https://img.shields.io/badge/Pytest-2CA5E0?style=for-the-badge&logo=pytest&logoColor=white)

___
### Как развернуть проект?<a name="start_project"></a>

* Клонировать репозиторий и перейти к файлам проекта

    ```
    git clone https://github.com/FakaFakaYeah/parser_python_pep.git
    ```

    ```
    cd src
    ```

* Создать и активировать виртуальное окружение:

    ```
    python -m venv venv
    source venv/Scripts/activate
    ```

* Установить файл с зависимостями

    ```
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    ```

___
## Аргументы(обязательные):<a name="required_arg"></a>

```
'pep': спарсить данные о документах PEP, получить статистику по каждому
статусу и общеее кол-во PEP документов
``` 

```
'whats-new': спрарсить данные о новостях версий Python
```

```
'latest-versions': спарсить данные о версиях Python
```

```
'download': скачать архив с докуметацией Python
```

___
## Аргументы(опциональные):<a name="arg"></a>
```
'-h' - вывод справки парсера со всеми аргументами
```

```
'-c', '--clear-cache': Очистка кэша
```

```
'-o', '--output': Дополнительные способы вывода данных (pretty, file).
Если аргумент не передан, то результат будет выведен в консоль.
```

___
## Примеры команд:<a name="cmd"></a>

* Спарсить статистику по PEP документам и сохранить в файл:

    ```
    python main.py pep -o file
    ```
  Файл с результатом будет хранится в директории results/

* Скачать архив с документацией Python:

    ```
    python main.py downloads
    ```
  Архив с документацией будет хранится в директории downloads/

* Спарсить данные о новостях Python в таблицу pretty:

    ```
    python main.py whats-new -o pretty
    ```

* Спарсить информацию о версиях Python в консоль
  
   ```
   python main.py latest-versions
   ```
  
___
### Авторы проекта:<a name="author"></a>
Смирнов Степан
<div>
  <a href="https://github.com/FakaFakaYeah">
    <img src="https://github.com/FakaFakaYeah/FakaFakaYeah/blob/main/files/images/GitHub.png" title="GitHub" alt="Github" width="39" height="39"/>&nbsp
  </a>
  <a href="https://t.me/s_smirnov_work" target="_blank">
      <img src="https://github.com/FakaFakaYeah/FakaFakaYeah/blob/main/files/images/telegram.png" title="Telegram" alt="Telegram" width="40" height="40"/>&nbsp
  </a>
</div>