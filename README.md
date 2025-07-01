📦 k8s_bot
k8s_bot — простой Telegram-бот на Python, развёрнутый в Kubernetes на Яндекс.Облаке с помощью CI/CD. Проект демонстрирует инфраструктурный подход к разработке, включая контейнеризацию, автоматическую сборку и деплой, работу с Secrets и Helm-чартами.

🚀 Возможности
Обработка команд через Telegram API

Ответ на /random — генерация случайного числа

Автоматический деплой через GitHub Actions

Развёртывание в Kubernetes кластере (Yandex.Cloud)

⚙️ Стек технологий
Компонент	Назначение
Python + python-telegram-bot	Логика Telegram-бота
Docker	Контейнеризация приложения
GitHub Actions	CI/CD и автодеплой
Kubernetes	Оркестрация и управление средой
Yandex.Cloud	Хостинг кластера
Helm	Управление конфигурацией деплоя

🛠 Установка и запуск локально
⚠ Требуется Python 3.10+ и установленный Poetry.

bash
Копировать
Редактировать
git clone https://github.com/DLgipp/k8s_bot.git
cd k8s_bot
poetry install
poetry run python bot.py
Создай .env файл или задай переменные окружения:

ini
Копировать
Редактировать
TELEGRAM_TOKEN=your_bot_token
📦 Контейнеризация
Сборка и запуск Docker-контейнера:

bash
Копировать
Редактировать
docker build -t k8s_bot .
docker run --rm -e TELEGRAM_TOKEN=your_token k8s_bot
☸ Развёртывание в Kubernetes
Установить Helm-чарт:

bash
Копировать
Редактировать
helm install k8s-bot ./helm/k8s-bot
Обновление:

bash
Копировать
Редактировать
helm upgrade k8s-bot ./helm/k8s-bot
Конфигурация Helm позволяет прокинуть токен через Kubernetes Secret.

🔄 CI/CD
Настроен pipeline через GitHub Actions:

Автоматическая сборка Docker-образа

Push в Yandex Container Registry

Автодеплой в кластер через kubectl

📁 Структура проекта
bash
Копировать
Редактировать
.
├── bot.py                # Основная логика Telegram-бота
├── Dockerfile            # Сборка контейнера
├── helm/                 # Helm-чарт для деплоя
├── .github/workflows/    # GitHub Actions для CI/CD
├── requirements.txt      # Зависимости (альтернатива poetry.lock)
└── README.md             # Документация
📌 Планы на развитие
 Логгирование и мониторинг через Prometheus + Grafana

 Больше команд (например, /help, /time, /joke)

 Отдельный backend под бота

 Тесты и покрытие CI

🧑‍💻 Автор
Разработано и поддерживается DLgipp
