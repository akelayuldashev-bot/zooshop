# 🐾 ZooShop

ZooShop — учебный Django-проект интернет-магазина товаров для питомцев.  
Проект реализован в рамках обучения и демонстрирует базовую архитектуру Django-приложения с пользовательским интерфейсом и бизнес-логикой.

---

## 🚀 Функционал

- 🛍 Каталог товаров
- ❤️ Добавление товаров в избранное
- 🛒 Корзина покупок
- 💬 Комментарии к товарам
- 💳 Тестовая платёжная система (Stripe / mock)
- 👤 Аутентификация пользователей
- 🎨 Кастомный дизайн и анимации

---

## 🧰 Стек технологий

- **Python 3**
- **Django**
- HTML / CSS / JavaScript
- SQLite (для разработки)
- Git & GitHub

---

## ⚙️ Установка и запуск (локально)

```bash
git clone https://github.com/akelayuldashev-bot/zooshop.git
cd zooshop
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
