# Django Internship Assignment Project

This project demonstrates a Django-based backend system with Django REST Framework, authentication, Celery for background task handling, and Telegram Bot integration.

## Features

- Django REST Framework APIs
- Token/JWT-based Authentication
- Celery with Redis for asynchronous background tasks
- Telegram bot that registers users via `/start`
- Secure production-ready configuration using `.env`
- Clean code structure with proper Git versioning

---

## Project Structure

```
project_root/
│
├── api/                      # Django app containing models, views, serializers
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
│
├── telegram_bot/
│   └── bot.py                # Telegram bot integration script
│
├── user_portal/              # Main Django project settings
│   ├── settings.py
│   └── urls.py
│
├── requirements.txt
├── .env
├── manage.py
└── README.md
```

---

## Setup Instructions

### 1. Clone the Repository

```
git clone https://github.com/YOUR_USERNAME/your-repo-name.git
cd your-repo-name
```

### 2. Create and Activate Virtual Environment

```
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory with the following content:

```
SECRET_KEY=your-django-secret-key
DEBUG=False
DATABASE_URL=sqlite:///db.sqlite3
TELEGRAM_BOT_TOKEN=your-telegram-bot-token
```

### 5. Run Migrations

```
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser (Optional)

```
python manage.py createsuperuser
```

### 7. Run Development Server

```
python manage.py runserver
```

---

## Telegram Bot Setup

1. Go to [https://t.me/BotFather](https://t.me/BotFather) in Telegram
2. Send `/newbot` and follow the instructions
3. Copy the bot token and paste it into your `.env` as `TELEGRAM_BOT_TOKEN`
4. Start the bot by running:

```
python telegram_bot/bot.py
```

5. Open your bot on Telegram and type `/start`. It will store your Telegram username and ID in the database.

---

## Background Task with Celery

### Setup Redis (required for Celery broker)

On Linux/Mac:
```
sudo apt install redis
sudo service redis start
```

On Windows: Use Redis for Windows from Memurai or Docker.

### Start Celery Worker

```
celery -A user_portal worker --loglevel=info
```

Example use case: sending email asynchronously after registration.

---

## API Endpoints

| Method | Endpoint         | Access      | Description                      |
|--------|------------------|-------------|----------------------------------|
| GET    | /api/public/     | Public      | Example public endpoint          |
| GET    | /api/protected/  | Auth only   | Requires token/JWT authentication |

Use tools like Postman or cURL for testing.

---

## Tech Stack

- Python
- Django
- Django REST Framework
- Redis
- Celery
- SQLite (default)
- Telegram Bot API

---

## Environment Variables Summary

| Variable             | Description                        |
|----------------------|------------------------------------|
| SECRET_KEY           | Django secret key                  |
| DEBUG                | Set to `False` for production      |
| DATABASE_URL         | Default: sqlite3                   |
| TELEGRAM_BOT_TOKEN   | Token from BotFather               |

---