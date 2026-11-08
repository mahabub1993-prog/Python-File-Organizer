# Python File Organizer

**A Python-based File Organization Solution with Desktop GUI and Web Application.**

Python File Organizer automatically organizes files into categories based on their file extensions. The project includes a Windows Desktop Application and a FastAPI-based Web Application.

## 🚀 Project Overview

Managing files manually can be time-consuming. This project simplifies file management by automatically sorting files into organized folders.

### Applications

**1. Desktop Application**
- Windows desktop application.
- Graphical User Interface (GUI).
- Automatic file organization.
- Categorizes files by extension.

**2. Web Application**
- Built with FastAPI.
- Upload multiple files through a browser.
- Automatically categorizes uploaded files.
- Supports files up to 100 MB per file.
- Upload progress indicator.
- Download all organized files as a ZIP archive.
- Simple and user-friendly interface.

**Web Application Source Code:**  
[Open File_Organizer_Web](./File_Organizer_Web/)

## 🛠️ Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| Desktop GUI | Python GUI |
| Web Framework | FastAPI |
| Backend Server | Uvicorn |
| Template Engine | Jinja2 |
| Frontend | HTML, CSS, JavaScript |
| Data Validation | Pydantic |
| Version Control | Git & GitHub |

## 📂 Project Structure

```text
Python-File-Organizer/
│
├── core/
│   ├── __init__.py
│   └── organizer.py
│
├── Customer_Delivery/
│
├── File_Organizer_Web/
│   ├── backend/
│   │   └── main.py
│   ├── templates/
│   │   └── index.html
│   ├── requirements.txt
│   └── README.md
│
├── file_organizer.py
├── file_organizer_gui.py
├── FileOrganizer.spec
├── .gitignore
└── README.md
```

## 💻 Run the Web Application Locally

### Prerequisites

- Python 3.10 or later
- Git

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/mahabub1993-prog/Python-File-Organizer.git
```

**2. Navigate to the Web Application folder**

```bash
cd Python-File-Organizer/File_Organizer_Web
```

**3. Create a virtual environment**

```bash
python -m venv venv
```

**4. Activate the virtual environment (Windows)**

```powershell
.\venv\Scripts\Activate.ps1
```

**5. Install dependencies**

```bash
pip install -r requirements.txt
```

**6. Start the application**

```bash
python -m uvicorn backend.main:app --reload
```

**7. Open in your browser**

Application:

http://127.0.0.1:8000

API Documentation:

http://127.0.0.1:8000/docs

## 🔌 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Web application dashboard |
| GET | `/health` | Application health check |
| GET | `/info` | Application information |
| POST | `/upload` | Upload and organize files |
| GET | `/download-all` | Download organized files as ZIP |

## 📋 File Categories

- Documents
- Images
- Spreadsheets
- Archives
- Videos
- Audio
- Others

## 🧪 Testing

The Web Application has been tested locally for:

- Multiple file uploads.
- Automatic file categorization.
- 95 MB file upload.
- ZIP archive download.
- ZIP extraction and file integrity.

## ☁️ Deployment Status

- Desktop Application: Developed.
- Web Application: Developed and locally tested.
- Cloud Deployment: Planned.

## 👨‍💻 Author

**Md. Mahabub Hossain**

GitHub: [mahabub1993-prog](https://github.com/mahabub1993-prog)

Project Repository: [Python-File-Organizer](https://github.com/mahabub1993-prog/Python-File-Organizer)

---

**Built with Python to make file management easier and more efficient.**
