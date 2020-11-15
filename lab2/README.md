### LAB_2
1. За допомогою пакетного менеджера *PIP* інсталювала pipenv та створила ізольоване середовище.
```
pip3 install pipenv
pipenv --python 3.8  
pipenv shell
```
2. Встановила бібліотеки *requests* та *ntplib* у своєму середовищі.
```
pipenv install requests
pipenv install ntplib
```
3. Переконалася що програма працює правильно.
```
python app.py
```
Результат:
```
========================================
Результат без параметрів: 
No URL passed to function
========================================
Результат з правильною URL: 
Time is:  09:40:24 AM
Date is:  11-15-2020
```
4. Встановила бібліотеку *pytest* та запустив тести, всі тести виконались успішно:
```
pipenv install pytest
pytest tests/tests.py
```
5. Дописала у програмі функцію, що перевіряє час доби на AM/PM та відповідно друкує "Доброго дня/вечора". Також написав тест який перевіряє правильність роботи функції.
6. Перенаправив результат виконання функції та тестів у файл results.txt:
```
pipenv run pytest tests/tests.py > results.txt
pipenv run python app.py append >> results.txt
```
