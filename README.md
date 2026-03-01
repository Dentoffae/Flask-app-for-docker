# Инструкция по сборке и запуску

## Требования

- Установленный [Docker](https://docs.docker.com/get-docker/)

## Сборка образа

В каталоге с проектом выполните:

```bash
docker build -t docker-test-app .
```

Имя образа `docker-test-app` можно заменить на любое другое.

## Запуск контейнера

```bash
docker run -p 5000:5000 docker-test-app
```

Приложение будет доступно по адресу: **http://localhost:5000**

## Эндпоинты

| Путь | Описание |
|------|----------|
| `GET /` | Статус приложения |
| `GET /info` | Информация о среде (Python, платформа) |
| `GET /multiply/<a>/<b>` | Умножение двух целых чисел |
| `GET /divide/<a>/<b>` | Деление двух чисел (b ≠ 0) |

## Примеры запросов

- http://localhost:5000/
- http://localhost:5000/info
- http://localhost:5000/multiply/6/7
- http://localhost:5000/divide/10/4

## Запуск в фоне

```bash
docker run -d -p 5000:5000 --name my-app docker-test-app
```

Остановка: `docker stop my-app`

## Очистка

```bash
docker stop my-app
docker rm my-app
docker rmi docker-test-app
```

---

# Docker Compose (backend + frontend)

В одном композе запускаются **Flask-бэкенд** и **веб-интерфейс** (nginx). Запросы к API идут внутри сети: браузер → frontend (порт 8080) → backend (внутри композа по имени `backend`).

## Запуск

```bash
docker compose up --build
```

Откройте в браузере: **http://localhost:8080**

На странице можно вызывать эндпоинты `/`, `/info`, `/multiply/<a>/<b>`, `/divide/<a>/<b>`. Запросы уходят на `/api/...`, nginx проксирует их на контейнер `backend:5000`.

## Остановка

```bash
docker compose down
```

