# Задание 5

1) В новом проекте, соответствующему базовому формату «проекта для автотестов», разработай автотест на заполнение и отправку формы https://demoqa.com/automation-practice-form
2) Запушь код в github-репозиторий и дай на него ссылку в качестве ответа на домашнее задание.
 - Условия:
   - Библиотеки, разрешенные к использованию: pytest, selene.
   - Тест должен жить в своем модуле python
   - Запрещено создавать свои собственные:
     - функции
       - кроме функции с тестом и опционально функции-фикстуры с настройкой браузера внутри conftest.py
     - переменные
     - дополнительные python модули кроме модуля с тестом
       - кроме опционального conftest.py

3) Учитывая ограничения, упомянутые выше – постарайся написать максимально читабельный и легкий в последующей поддержке код. В основном это будет касаться именно подбора локаторов для нахождения соответствующих элементов.
4) Обрати внимание на то, что твоя задача – написать тест, а не скрипт с шагами;) 
5) Также, если это твои первые шаги в автоматизации, постарайся максимально симулировать реальные действия пользователя, например при работе с контролом выбора даты рождения – автоматизируй полностью выбор даты, а не просто впиши ее в поле. Это касается и других полей в форме, например селектов (дропдаунов).

## Краткая шпаргалка по основным командам Selene

Если добавить строку `browser.config.set_value_by_js = True` - и например прописать это в конфиге вместе с настройками браузера <br>
то текст будет не пропечатываться по символьно, а вставляться блоком. что ускоряет тест. Например длинный адрес и тд.

или вставить в самом коде используя после элемента `with_(set_value_by_js = True)`

`browser.element(selector)` - находит элемент по селектору

`- element.element(selector)` находит внутренний элемент внутри другого элемента обозначенного как element (например сохраненного как element = browser.element(selector))

`- element.all(selector)` находит внутреннюю коллекцию элементов

`browser.all(selector)` - находит коллекцию элементов по селектору

`- collection.by(condition)` - фильтрует коллекцию по кондишену (где collection - сохраненная коллекция например через collection = browser.all(selector); condition – что либо из be.* или have.*)

`- collection.element_by(condition)` - находит элемент коллекции по кондишену

`- collection[index]` или `collection.element(index)` - выбирает элемент из коллекции по индексу (есть шорткаты – .first для [0] и .second для [1])

`- collection[start:stop:step]` - делает срез коллекции начиная со start, заканчивая перед stop, с шагом step (есть шорткаты – .odd для [::2] и .even для [1::2]; есть алиас sliced(start, stop, step) для [start:stop:step])

`(element | collection| browser).should(condition)` - ждет до выполнения условия и падает если не проходит

`(element | collection | browser).wait_until(condition)` - ждет до выполнения условия и возвращает false если не проходит, иначе true

`(element | collection | browser).matching(condition)` - сразу проверяет условие и возвращает false если не проходит, иначе true

Команды типа ...
- `* collection.by_their(selector, condition)`

- `* collection.element_by_its(selector, condition)`

- `* collection.all(selector)`

- `* collection.all_first(selector)`

... – используются реже, и доки на них можно почитать провалившись в их реализацию (там есть детальные docstrings). Также ниже можно найти примеры и разборы этих команд в FAQ в прикрепленном сообщении в этом чате как ответ на вопрос «Как найти нужною строку в таблице по условию ...»

Скрипт, позволяющий устанавливать масштаб страницы ( не разрешение!!) например 60% 

```commandline
browser.execute_script('document.querySelector(".body-height").style.transform = "scale(.6)"')
```

Более подробная информация по Selene

[Selene Wiki](https://github.com/MDN78/qa_guru_python_10_5/wiki)