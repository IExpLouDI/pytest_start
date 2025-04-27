# Summarize dataframe

Опции запуска pytest

-v предоставляет более развернутую информацию по итогам.

--collect-only показывает, какие тесты будут выполняться с заданными
параметрами и конфигурацией

-k позволяет использовать выражение для определения функций тестирования.
pytest -k "asdict or defaults"

-m способ отметить подмножество тестовых функций для
совместного запуска.

Маркеры необходимо добавить в pyproject.toml
пример:
```rb
[tool.pytest.ini_options]
        markers = [
            "slow: marks tests as slow (deselect with '-m "not slow"')",
            "serial",
        ]
```

Тесты помечаются 
```rb
@pytest.mark.run_these_please
```
Запуск
```rb
pytest -m run_these_please 
pytest -m "mark1 and not mark2"
pytest -m "mark1 or mark2"
```

-x Если тестовая функция обнаружит сбой assert или exception, выполнение этого теста
останавливается, и тест завершается ошибкой.

--maxfail=num параметр, чтобы указать, сколько ошибок допускается получить

--tb=style изменяет способ вывода пакетов трассировки для сбоев. 
style = short печатает только строку assert и символ E без контекста; 
style = line сохраняет ошибку в одной строке; 
style = no полностью удаляет трассировку.

-s позволяет печатать операторы — или любой другой вывод, который обычно
печатается в stdout

--lf способ выполнения только неудачных тестов
полезен для отладки

-q сокращает объем информации в
отчете. Удобно использовать его в сочетании с --tb=line, в этом случае
выводятся только неудавшиеся строки любых неудачных тестов.

-l локальные переменные и их значения
отображаются вместе с tracebacks для неудачных тестов.

--durations=N полезна, когда вы пытаетесь ускорить свой набор
тестов. Она не меняет ваши тесты; сообщает самый медленный N номер
tests/setups/teardowns по окончании тестов. Если вы передадите --durations=0, он
сообщит обо всем в порядке от самого медленного к самому быстрому.

Запустить все тесты из одного каталога
```rb
pytest tests\func --tb=no
```

-v показывает синтаксис для запуска определенного каталога, класса и теста.
```rb
pytest -v tests\func --tb=no
Результат
ests\func\test_add_variety.py::test_add_2[task2] PASSED
tests\func\test_add_variety.py::test_add_2[task3] PASSED
tests\func\test_add_variety.py::test_add_3[sleep-None-False] PASSED
tests\func\test_unique_id_4.py::test_unique_id_is_a_duck xfail
tests\func\test_unique_id_4.py::test_unique_id_not_a_duck XPASS
```

Чтобы запустить файл, полный тестов
```rb
pytest tests/func/test_add.py
```

Чтобы запустить одну тестовую функцию
```rb
pytest -v tests/func/test_add.py::test_add_returns_valid_id
```
