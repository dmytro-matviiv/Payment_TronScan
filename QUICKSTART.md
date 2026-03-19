# 🚀 Швидкий старт

## Крок 1: Встановлення

```bash
pip install -r requirements.txt
```

## Крок 2: Налаштування

Створіть файл `.env` та додайте:

```
TELEGRAM_BOT_TOKEN=8456055614:AAEQcO_4iS3wnJ6ooZ-2BbgWsHSfFnWsPco
TELEGRAM_CHANNEL_ID=@your_channel
TRONSCAN_API_TOKEN=3bfa787b-22a1-4c79-a2f5-b46dc062ee9f
TRON_ADDRESS=TYY4QoQ8nA4geSoYpueQ14DLFnHhYBKCiR
CHECK_INTERVAL=30
```

## Крок 3: Отримання Channel ID

```bash
python get_channel_id.py
```

Або використайте username каналу (наприклад: `@your_channel`)

## Крок 4: Додавання бота в канал

1. Відкрийте ваш Telegram канал
2. Перейдіть в Налаштування → Адміністратори
3. Додайте бота `@DP_payment_bot` як адміністратора
4. Надайте права на відправку повідомлень

## Крок 5: Запуск

```bash
python bot.py
```

Готово! Бот почне моніторити платежі та відправляти повідомлення в канал.

---

**Примітка:** Якщо виникають проблеми, перевірте README.md для детальних інструкцій.

