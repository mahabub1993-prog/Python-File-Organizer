# Python File Organizer

**Smart File Management | Desktop Application | Web Application**

A Python-based file management solution that automatically organizes files into categories. This repository contains a Windows Desktop Application and a browser-based Web Application developed with FastAPI.

## Project Highlights

- **Desktop Application:** Organize files on a Windows computer using a graphical interface.
- **Web Application:** Upload multiple files, automatically categorize them, and download the organized files as a ZIP archive.
- **Automation:** Reduce repetitive manual file-management tasks.
- **Open Development:** Source code and project documentation are maintained in this repository.

## Applications

### 1. Desktop File Organizer

A Windows desktop application for organizing files automatically.

**Features**
- Graphical user interface.
- Automatic file categorization by file extension.
- Separate folders for different file types.
- CSV organization report.
- Ready-to-use Windows executable.

**Customer delivery files:** `Customer_Delivery/`

### 2. Smart File Organizer — Web Application

A browser-based file organizer powered by Python and FastAPI.

**Features**
- Upload one or multiple files.
- Automatically categorize uploaded files.
- Organize files into category-based folders.
- Download all organized files in a ZIP archive.
- Browser-based user interface.
- REST API with Swagger documentation.
- Maximum configured file size: 100 MB per file.

**Supported categories**

| Category | Example file types |
|---|---|
| Documents | PDF, DOC, DOCX, TXT |
| Images | JPG, JPEG, PNG, GIF |
| Spreadsheets | XLS, XLSX, CSV |
| Archives | ZIP, RAR, 7Z |
| Videos | MP4, AVI, MKV |
| Audio | MP3, WAV |
| Others | Other supported file extensions |

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| FastAPI | Web application backend |
| Uvicorn | ASGI server |
| Jinja2 | HTML templating |
| HTML, CSS, JavaScript | Web interface |
| Pandas | CSV reporting |
| ZIP | Download organized files |
| Git & GitHub | Version control and source hosting |

## Repository Structure

```text
Python-File-Organizer/
│
├── Customer_Delivery/
│   ├── FileOrganizer.exe
│   ├── README.txt
│   └── User_Guide.txt
│
├── core/
│   ├── __init__.py
│   └── organizer.py
│
├── File_Organizer_Web/
│   ├── backend/
│   │   └── main.py
│   ├── templates/
│   │   └── index.html
│   ├── static/
│   ├── tests/
│   ├── uploads/
│   ├── requirements.txt
│   └── README.md
│
├── file_organizer.py
├── file_organizer_gui.py
├── FileOrganizer.spec
├── .gitignore
└── README.md
```

## Run the Web Application Locally

### Requirements

- Python 3.10 or newer
- pip
- Git

### 1. Clone the repository

```bash
git clone https://github.com/mahabub1993-prog/Python-File-Organizer.git
```

### 2. Open the Web Application directory

```bash
cd Python-File-Organizer/File_Organizer_Web
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the environment

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Start the application

```bash
python -m uvicorn backend.main:app --reload
```

### 7. Open the application

| Service | URL |
|---|---|
| Web Application | http://127.0.0.1:8000 |
| Swagger API Docs | http://127.0.0.1:8000/docs |
| ReDoc | http://127.0.0.1:8000/redoc |

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Web application homepage |
| GET | `/health` | Health check |
| GET | `/info` | Application information |
| POST | `/upload` | Upload and organize files |
| GET | `/download-all` | Download organized files as ZIP |

## Testing and Validation

The Web Application has been tested locally for:

- Single-file and multiple-file uploads.
- Automatic file categorization.
- ZIP archive generation and download.
- Extraction and verification of downloaded ZIP contents.
- A large-file upload test using a 95 MB file.

## Project Status

| Component | Status |
|---|---|
| Desktop Application | Developed |
| Web Application | Developed and locally tested |
| GitHub Repository | Published |
| Cloud Deployment | Planned |
| Additional Automation Features | Planned |

**Note:** Cloud deployment is not yet claimed as completed. Deployment and production storage configuration will be documented after implementation.

## Future Development

- Cloud deployment.
- User authentication and account management.
- Customer-specific file management.
- Persistent cloud storage integration.
- Additional file-processing and automation features.
- Improved testing and production monitoring.

## About the Developer

**Md. Mahabub Hossain**

Python Automation | AI Automation | Telecom Engineering

- **GitHub:** https://github.com/mahabub1993-prog
- **LinkedIn:** https://www.linkedin.com/in/md-mahabub-hossain-0846ab222

---

*Python File Organizer — Making File Management Simple and Automatic.*
