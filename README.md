<div align="center">

# 🏔️ Visit Nepal 2022

**A full-stack travel guide web application for exploring Nepal — with hotel booking, a community gallery, an AI chatbot, and threaded community posts.**

[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white)](https://python.org)
[![Django](https://img.shields.io/badge/Django-3.2%2B-092E20?logo=django&logoColor=white)](https://djangoproject.com)
[![Rasa](https://img.shields.io/badge/Rasa-3.x-5A17EE?logo=rasa&logoColor=white)](https://rasa.com)
[![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?logo=sqlite&logoColor=white)](https://sqlite.org)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

</div>

---

## ✨ Features

| Module | Description |
|---|---|
| 🗺️ **Explore Nepal** | Swiper.js carousel showcasing Nepal's top destinations |
| 🏛️ **Culture, Nature & Sports** | Category pages with admin-managed posts and threaded comments |
| 🖼️ **Community Gallery** | User-uploaded photo gallery with glassmorphic lightbox viewer |
| 🏨 **Hotel Booking** | Browse Normal / Delux / Premium room categories, check availability, and book instantly |
| 🤖 **AI Chatbot** | Rasa-powered NLP assistant answering Nepal travel FAQs |
| 👤 **Member Dashboard** | Profile management, photo uploads, booking history |
| 🔐 **Auth System** | Animated login/register with Google & Facebook social buttons, toast notifications |

---

## 📁 Project Structure

```
Visit_Nepal_2022-main/
│
├── django_app/                     ← Django web application
│   ├── manage.py
│   ├── db.sqlite3
│   ├── static/                     ← CSS, fonts, images
│   ├── media/                      ← User-uploaded files
│   ├── templates/                  ← Global base template
│   │
│   ├── Visit_Nepal_2022/           ← Django project config
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── asgi.py
│   │
│   ├── pages/                      ← Explore, Culture, Nature, Sport, Gallery views
│   ├── pages_content/              ← Post & Comment models, threaded comment views
│   ├── login_register/             ← User authentication (login, register, logout)
│   ├── members/                    ← User dashboard, photo uploads, booking history
│   ├── chatbot/                    ← Rasa chatbot Django interface
│   └── hotel_management_system/    ← Room categories, room listings, booking engine
│
├── rasa_bot/                       ← Rasa NLP chatbot server
│   ├── config.yml                  ← NLU pipeline & policy config
│   ├── domain.yml                  ← Intents, responses, session settings
│   ├── data/
│   │   ├── nlu.yml                 ← Training phrases
│   │   ├── stories.yml             ← Conversation flows
│   │   └── rules.yml               ← Hard-coded conversation rules
│   ├── actions/
│   │   └── actions.py              ← Custom server-side actions
│   └── models/                     ← Trained Rasa models (auto-generated)
│
├── run_all.py                      ← One-command launcher (Django + Rasa)
└── README.md
```

---

## 🛠️ Prerequisites

- **Python** 3.9 or higher
- **pip** (comes with Python)
- A virtual environment tool (`venv` or `conda`)
- **Rasa** 3.x — *requires a separate environment* (see note below)

> [!NOTE]
> Rasa has strict dependency requirements that often conflict with Django packages.  
> It is strongly recommended to install Rasa in its **own dedicated conda/venv environment**.

---

## 🚀 Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Visit_Nepal_2022.git
cd Visit_Nepal_2022-main
```

### 2. Set Up Django Environment

```bash
# Create and activate a virtual environment
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate

# Install Django dependencies
pip install django Pillow
```

### 3. Configure & Run Django

```bash
cd django_app

# Apply database migrations
python manage.py migrate

# (Optional) Create a superuser for the Admin panel
python manage.py createsuperuser

# Collect static files (for production only)
# python manage.py collectstatic

# Start the development server
python manage.py runserver
```

The Django site will be live at **http://127.0.0.1:8000**

---

### 4. Set Up Rasa Chatbot (Optional — Separate Environment)

```bash
# It is recommended to use a separate conda environment for Rasa
conda create -n rasa-env python=3.9
conda activate rasa-env

pip install rasa

cd rasa_bot

# Train the NLP model (required before first run)
rasa train

# Start the Rasa API server
rasa run -m models --enable-api --cors "*"
```

The Rasa server will be available at **http://localhost:5005**

---

### 5. One-Command Launch (Both Servers)

If Rasa is installed in the same environment as Django, you can start both with:

```bash
# From the repository root
python run_all.py
```

This will:
1. Start the **Rasa chatbot** server on port `5005`
2. Start the **Django web server** on port `8000`
3. Monitor both processes and shut down cleanly on `Ctrl+C`

---

## 🗂️ Django Admin Panel

Access the admin panel at **http://127.0.0.1:8000/admin/**

From here you can:
- ➕ Add/edit **Posts** (with category, image, description)
- 🏷️ Manage **Categories** (Culture, Nature, Sport)
- 🏨 Add/edit **Room Categories** and **Rooms** (with images and pricing)
- 🖼️ Review **community photo uploads**
- 👥 Manage **users**

---

## 🧩 Key URL Routes

| URL | Description |
|---|---|
| `/` | Homepage / Explore Nepal |
| `/culture` | Culture section |
| `/natural` | Nature section |
| `/sport` | Sports section |
| `/gallery` | Community photo gallery |
| `/post?id=<n>` | Individual post with threaded comments |
| `/login/` | Login & Register (sliding animated form) |
| `/members` | User dashboard |
| `/room_cat` | Hotel room category overview |
| `/seperateroom/<Category>` | Room listings + booking form |
| `/chatbotinterface` | AI travel chatbot |
| `/admin/` | Django admin panel |

---

## 🏗️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | Django 3.2+ |
| Database | SQLite (dev) / PostgreSQL (recommended for prod) |
| Frontend | Vanilla HTML, CSS, JavaScript |
| Carousel | Swiper.js |
| Icons | Font Awesome 6 |
| Chatbot | Rasa Open Source 3.x |
| Media Storage | Django media files (local) |
| Auth | Django built-in auth + session management |

---

## 📸 Pages Overview

- **Explore Nepal** — Hero cover + Swiper carousel of destinations + feature image grid
- **Culture / Nature / Sports** — Category posts with image cards, click to view full post with comments
- **Gallery** — Masonry photo grid, click for glassmorphic lightbox modal
- **Hotel Rooms** — 3-column category cards → room detail + sticky booking reservation form
- **Member Dashboard** — Profile info, booking history cards, photo upload manager
- **Login / Register** — Full-screen animated slide-in/out panels, social auth buttons, toast alerts

---

## 🔧 Development Notes

- Dark / Light mode is fully supported across all pages — toggle via the navbar icon
- Toast notifications (5-second auto-dismiss) appear on all form actions: login, register, booking, comment, photo upload/delete
- Threaded comments (2 levels deep) with Reddit-style branching connectors
- Hotel booking validates date conflicts automatically via `check_availability()`

---

## 📄 License

This project is developed as a **Final Year Project (FYP)** by **Prashant**.

© 2026 Visit Nepal 2022. All Rights Reserved. Developed by Prashant.
