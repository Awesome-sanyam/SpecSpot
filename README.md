# SpecSpot 📱✨

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Django](https://img.shields.io/badge/django-5.2+-green.svg)](https://www.djangoproject.com/)

SpecSpot is an intelligent, AI-powered mobile phone discovery and specification platform. Powered by Google Gemini, SpecSpot helps users find the perfect smartphone based on their unique requirements, while providing an extensive database of phone specifications, technical glossaries, and community feedback.

---

## 🚀 Features

- **AI Phone Finder**: Tell the AI what you're looking for (e.g., "Best camera phone under $500"), and Gemini will analyze your request to recommend the best options along with a detailed summary.
- **Comprehensive Specifications**: Browse through a curated database of popular smartphones, viewing detailed specs including RAM, Processor, Camera, Display Type, and more.
- **Tech Glossary**: Not sure what "AMOLED" or "Snapdragon" means? Our built-in tech glossary explains jargon simply.
- **User Feedback & Community**: Log in to share your feedback. The community's latest thoughts are highlighted directly on the homepage.
- **Responsive Design**: Clean and modern UI that works across desktop and mobile devices.

## 🛠️ Technology Stack

- **Backend**: Python, Django
- **Database**: SQLite (Default)
- **AI Integration**: Google Generative AI (Gemini)
- **Frontend**: HTML, CSS, JavaScript (Vanilla)

## 💻 Local Development Setup

Follow these steps to get a local copy of SpecSpot up and running on your machine.

### Prerequisites
- Python 3.8+
- Git

### 1. Clone the repository
```bash
git clone https://github.com/Awesome-sanyam/SpecSpot.git
cd SpecSpot
```

### 2. Create a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Copy the `.env.example` file to `.env`:
```bash
cp .env.example .env
```
Open `.env` and add your **Google Gemini API Key**:
```env
GEMINI_API_KEY=your_actual_api_key_here
```

### 5. Run Migrations & Start the Server
```bash
cd SpecSpot
python manage.py migrate
python manage.py runserver
```

Open your browser and navigate to `http://127.0.0.1:8000` to see the application running!

## 🤝 Contributing
Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**. 
Please read our [Contributing Guidelines](CONTRIBUTING.md) for more details.

## 📜 License
Distributed under the MIT License. See `LICENSE` for more information.

## 📫 Contact
Sanyam Gehlot - [GitHub Profile](https://github.com/Awesome-sanyam)
Project Link: [https://github.com/Awesome-sanyam/SpecSpot](https://github.com/Awesome-sanyam/SpecSpot)
