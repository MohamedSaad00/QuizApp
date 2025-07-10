# Flask Quiz App

A fully responsive quiz application built using Python's Flask framework for the backend and basic HTML/CSS for the frontend.

- [Report a Bug](https://github.com/MohamedSaad00/QuizApp/issues)
- [Request a Feature](https://github.com/MohamedSaad00/QuizApp/issues)

---

## 📚 Table of Contents

1. [About the Project](#💡-about-the-project)
2. [Features](#✅-features)
3. [Built With](#🛠️-built-with)
4. [Getting Started](#🚀-getting-started)
5. [Usage](#💻-usage)
6. [Contributing](#🤝-contributing)
7. [License](#📄-license)
8. [Contact](#📬-contact)

---

## 💡 About the Project

This is a simple yet powerful Flask-based Quiz Application. It allows users to register, take quizzes, see their scores instantly, and compete with other users for the highest score.

## 📽️ Project Demo Video

Watch the full demo here:

➡️ [Click to Watch on YouTube](https://youtu.be/vpatgXiygQ8)

---

## ✅ Features

- 🔐 Login & Registration
- 🔁 Retake quizzes
- 📊 View scores immediately
- 🏆 Leaderboard (highest score by user)
- 💾 Uses SQLite for local data storage
- 📱 Responsive front-end layout

---

## 🛠️ Built With

- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- Basic HTML & CSS
- SQLAlchemy + Alembic for migrations

---

## 🚀 Getting Started

Follow these instructions to get the project running on your local machine.

### 📋 Prerequisites

Make sure you have:

- Python 3.6+
- pip (Python package manager)
- Git
- virtualenv (optional but recommended)

---

### ⚙️ Installation Steps

```bash
# 1. Clone the repository
git clone https://github.com/MohamedSaad00/QuizApp.git
cd QuizApp

# 2. Create a virtual environment and activate it
python -m venv venv
venv\Scripts\activate             # On Windows
# OR
source venv/bin/activate          # On Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set environment variables (for development)
set FLASK_APP=app
set FLASK_DEBUG=1
# OR (Unix/macOS)
export FLASK_APP=app
export FLASK_DEBUG=1

# 5. Run database migrations
flask db init                    # Only the first time
flask db migrate -m "Initial migration"
flask db upgrade

# 6. Start the app
flask run
```

## 💻 Usage

This app is ideal for schools, educators, or internal company training tools. Users register, take tests, and get immediate feedback with a competitive leaderboard experience.

## 🤝 Contributing

Contributions make the community stronger! To contribute:

1. Fork the repository
2. Create your branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to your branch (`git push origin feature/AmazingFeature`)
5. Create a new Pull Request

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for more info.

## 📬 Contact

**Name:** Mohamed Saad  
**GitHub:** [MohamedSaad00](https://github.com/MohamedSaad00)  
**Project Link:** [QuizApp](https://github.com/MohamedSaad00/QuizApp)
