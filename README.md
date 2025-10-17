# GoIT CS HW-02

## Завдання 1: Bash скрипт для моніторингу доступності вебсайтів

### Опис
Скрипт `website_availability_healthcheck.sh` перевіряє доступність списку вебсайтів та логує результати.

### Використання

```bash
chmod +x scripts/website_availability_healthcheck.sh
./scripts/website_availability_healthcheck.sh
```

### Що робить скрипт

- Перевіряє HTTP статус кожного сайту зі списку
- Логує результати у файл `website_status.log`
- Виводить повідомлення про завершення

### Приклад виводу в лог

```
<https://google.com> is UP
<https://facebook.com> is UP
<https://whyicannotfindit.com> is DOWN
```

## Завдання 2: Docker Compose з FastAPI та PostgreSQL

### Опис
Створення Docker Compose конфігурації для запуску FastAPI додатку з PostgreSQL базою даних.

### Запуск проекту

1. Переконайтеся, що Docker і Docker Compose встановлені на вашій системі

2. Клонуйте репозиторій:
```bash
git clone <repository-url>
cd goit-cs-hw-02
```

3. Запустіть контейнери:
```bash
docker-compose up --build
```

4. Додаток буде доступний за адресою:
   - FastAPI: http://localhost:8000
   - PostgreSQL: http://localhost:5432

5. Для зупинки контейнерів:
```bash
docker-compose down
```


