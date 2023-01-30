# Скрапер документов PEP

[Описание](#описание) /
[История изменений](#история-изменений) /
[Развернуть локально](#развернуть-локально) /
[Документация](#документация) /
[Автор](#автор) /


## Описание

Скрапер [scrapy_parser_pep](https://github.com/avtorsky/scrapy_parser_pep) собирает документы PEP с ресурса [https://peps.python.org/](https://peps.python.org/) и формирует результат двух типов:

* pep_{datetime}.csv - список всех PEP (номер, название и статус)
* status_summary_{datetime}.csv - сводка по статусам PEP, сколько найдено документов в каждом статусе (статус, количество)

## История изменений

Release 20230130:
* feat(./pep_parse): подготовлен паук для скраппинга документов PEP и настроен пайплайн обработки айтемов

## Развернуть локально

Склонировать проект, создать виртуальное окружение и проинициализировать зависимости:

```bash
git clone https://github.com/avtorsky/scrapy_parser_pep.git
cd scrapy_parser_pep
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

## Документация

Парсер запускается из root-директории проекта командой

```bash
scrapy crawl pep
```

## Автор

[@avtorsky](https://github.com/avtorsky)
