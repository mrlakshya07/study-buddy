# 🍅 Smart Study Assistant (Study Buddy)

A comprehensive web-based study management system built with Flask that helps students organize their study sessions, take notes, track progress, and maintain focus using the Pomodoro technique.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📋 Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## ✨ Features

### 📝 **Notes Management**
- Add timestamped notes with automatic date tracking
- View all saved notes in an organized interface
- Search notes by keywords
- Delete unwanted notes
- Simple and intuitive note-taking interface

### 📊 **Study Progress Tracker**
- Log study sessions with date and duration
- View historical study data
- Visualize progress with interactive charts using Matplotlib
- Calculate average study time per day
- Track your study consistency over time

### 🍅 **Pomodoro Timer**
- Customizable timer for focused study sessions (default: 25 minutes)
- Visual countdown display with large, easy-to-read numbers
- Alarm notification when timer completes
- Start, stop, and reset functionality
- Sound test feature to ensure notifications work
- Beautiful purple-themed interface

### 🔐 **User Authentication**
- Secure login and signup system
- User session management
- Protected routes

## 🛠️ Technologies Used

- **Backend:** Python 3.8+, Flask
- **Frontend:** HTML5, CSS3, JavaScript
- **Data Visualization:** Matplotlib
- **Storage:** File-based storage (notes.txt, study_log.txt)
- **Audio:** HTML5 Audio API
- **Version Control:** Git, GitHub

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

### Step-by-Step Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/study_buddy.git
   cd study_buddy
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install required packages**
   ```bash
   pip install flask matplotlib
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser**
   ```
   Navigate to: http://127.0.0.1:5000
   ```

## 🚀 Usage

### First Time Setup

1. **Sign Up:** Create a new account on the login page
2. **Login:** Enter your credentials to access the main menu

### Using Features

#### **Notes**
- Click **"Add Notes"** from the menu
- Type your note and click **Save**
- Notes are automatically timestamped
- View, search, or delete notes as needed

#### **Study Progress**
- Click **"Study Progress"** from the menu
- Click **"Log Study Session"** to record your study time
- Enter the date and hours studied
- View your progress chart showing average study time per day
- Track your consistency and improvement over time

#### **Pomodoro Timer**
- Click **"Pomodoro Timer"** from the menu
- Click **"Test Sound"** to ensure alarm notifications work
- Set your desired study duration (default: 25 minutes)
- Click **"▶️ Start Timer"** and focus on your work
- When timer completes, you'll hear an alarm sound
- Click **"🔄 Start New Timer"** to begin another session

## 📁 Project Structure

```
study_buddy/
│
├── app.py                      # Main Flask application
├── notes.py                    # Notes management module
├── study_progress_tracker.py   # Progress tracking module
├── pomodoro.py                 # Pomodoro timer module
├── README.md                   # Project documentation
│
├── templates/                  # HTML templates
│   ├── index.html             # Login/signup page
│   ├── notes.html             # Notes interface
│   ├── progress.html          # Progress visualization
│   ├── progress_log.html      # Study session logging
│   └── pomodoro.html          # Pomodoro timer
│
├── static/                     # Static files
│   └── alarm.mp3              # Timer alarm sound
│
├── notes.txt                   # Stored notes (auto-created)
└── study_log.txt              # Study session logs (auto-created)
```

## 🎯 Key Highlights

- **All-in-One Solution:** Notes, progress tracking, and Pomodoro timer in a single application
- **Easy to Use:** Clean, intuitive interface designed for students
- **No Database Required:** Simple file-based storage makes it easy to deploy
- **Visual Progress:** See your study habits improve with interactive charts
- **Focus Mode:** Built-in Pomodoro timer helps maintain concentration
- **Fully Offline:** Works completely offline after initial setup

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
5. Push to the branch (`git push origin feature/AmazingFeature`)
6. Open a Pull Request

### Ideas for Contributions

- Add database support (SQLite/PostgreSQL)
- Implement quiz generation feature
- Add dark mode toggle
- Create mobile-responsive design
- Add calendar view for study sessions
- Implement data export functionality (CSV, PDF)
- Add study goal setting and tracking
- Integrate with Google Calendar

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Contact

**Your Name**

- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourprofile)
- Email: your.email@example.com

## 🎯 Motivation

As a B.Tech student, I found it challenging to manage my study time, take organized notes, and maintain focus during study sessions. This project was born from the need to have an all-in-one study management tool that combines note-taking, progress tracking, and the proven Pomodoro technique in a simple, easy-to-use interface.

## 🙏 Acknowledgments

- Pomodoro Technique by Francesco Cirillo
- Built as a B.Tech engineering project
- Inspired by the need for better student productivity tools
- Thanks to the open-source community for Flask and Matplotlib

## 📝 Future Enhancements

- [ ] Add user profile customization
- [ ] Implement database storage (SQLite/PostgreSQL)
- [ ] Add mobile app version
- [ ] Include flashcard feature
- [ ] Integrate AI-powered study recommendations
- [ ] Add collaborative study rooms
- [ ] Export notes to PDF
- [ ] Add break timer between Pomodoro sessions
- [ ] Statistics dashboard with weekly/monthly views
- [ ] Study streak tracking
- [ ] Custom alarm sounds

## 🐛 Known Issues

- Timer alarm sound requires user interaction first (browser security policy)
- No data persistence across different user sessions
- Limited to single-user usage in current version

## 📊 Project Statistics

- **Lines of Code:** ~1000+
- **Development Time:** 2-3 weeks
- **Technologies Learned:** Flask, Web Development, Data Visualization, JavaScript

---

⭐ **If you found this project helpful, please give it a star!** ⭐

---

**Made with ❤️ by [Your Name]**

*Project Status: In Development 🚧*