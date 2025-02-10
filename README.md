
# Пример Fluentd как шина для HTTP сервисов

Детальное описание работы в статье: [Fluentd как шина для HTTP сервисов](https://byurrer.ru/fluentd-as-bus-for-http).

Репозиторий показывает как можно использовать Fluentd для гарантированной доставки `JSON` из одной системы в другую через Fluentd - попытка использовать Fluentd как шину данных.

В этом примере есть 2 контейнера:
* **Fluentd**: настроен на прием данных и переотправку по `HTTP` с гарантированной доставкой
* **http**: скрипт на Python для поднятия `HTTP-сервера` (`server.py`), выводит все что приходит в консоль

Запустить композицию контейнеров:
```bash
docker compose up -d
```

Кроме контейнеров есть скрипт `send.py` для отправки сообщения во Fluentd. Запустить отправку тестового события во Fluentd:
```bash
docker exec -it 2http-fluentd-http-1 python3 send.py
```

После отправки сообщения во Fluentd оно должно сразу переотправиться на `HTTP-сервер` (*если контейнер запущен, иначе оно буферизируется и будет отправлено позже*) и будет выведено в логи контейнера:

```
fluend-1  | 2025-02-09 14:34:40 +0000 [debug]: #0 Created new chunk chunk_id="62db67ded9217786498e8c3658bbca29" metadata=#<struct Fluent::Plugin::Buffer::Metadata timekey=nil, tag="api.path", variables=nil, seq=0>
fluend-1  | 2025-02-09 14:34:40 +0000 [debug]: #0 Post data to http://http:8000/api/path/ with chunk(62db67ded9217786498e8c3658bbca29)
http-1    | 
http-1    | Body: {"message":"Hello, Fluentd!","status":"ok"}
http-1    | 
http-1    | 172.24.0.3 - - [09/Feb/2025 14:34:40] "POST /api/path/ HTTP/1.1" 200 -
fluend-1  | 2025-02-09 14:34:40 +0000 [debug]: #0 200 OKHello from POST!
```
