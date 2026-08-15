<div align="center">

# 🏔️ Visit Nepal 2022

**A full-stack travel guide web application for exploring Nepal — with hotel booking, a community gallery, an AI chatbot, and threaded community posts.**

![Nepal Giphy GIF](https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExdDUxZ2o0NmpzYWZnemJ3aHRmeTZoMzJ5aDJubWE2cmlpOGE3bDhpOCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/PjatleHkNdPP3J7brX/giphy.gif)

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
├── installme.bat                   ← One-click Windows Installer
├── installme.sh                    ← One-click Linux/macOS Installer
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

## 🚀 Setup & Installation (Automated)

Setting up the project is fully automated via installer scripts.

### 1. Clone the Repository

```bash
git clone https://github.com/prashantshreh-pixel/Visit-Nepal-2022.git
cd Visit-Nepal-2022
```

### 2. Run the Installer

#### 💻 Windows
Double-click `installme.bat` or run:
```cmd
installme.bat
```

#### 🍎 macOS / 🐧 Linux
Run:
```bash
chmod +x installme.sh
./installme.sh
```

The installer script will:
- Set up a Python virtual environment (`venv`).
- Activate it and install dependencies from `requirements.txt`.
- Set up the SQLite database and run Django migrations.

---

### 3. Run the Servers

Once installed, start the local servers with:

```bash
# Activate the environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Run both servers (Django + Rasa Chatbot)
python run_all.py
```

This starts:
1. **Django web server** on **http://127.0.0.1:8000**
2. **Rasa chatbot** server on **http://localhost:5005**

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

## 🔧 Development Notes

- Dark / Light mode is fully supported across all pages — toggle via the navbar icon
- Toast notifications (5-second auto-dismiss) appear on all form actions: login, register, booking, comment, photo upload/delete
- Threaded comments (2 levels deep) with Reddit-style branching connectors
- Hotel booking validates date conflicts automatically via `check_availability()`

---

## 📄 License

This project is developed as a **Final Year Project (FYP)** by **Prashant**.

© 2026 Visit Nepal 2022. All Rights Reserved. Developed by Prashant.
