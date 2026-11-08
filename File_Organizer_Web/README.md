# Python File Organizer

**Automated File Management System | Desktop & Web Applications**

A Python-based file management solution that automatically organizes files into categories. This project includes a Windows Desktop Application and a Web Application built with FastAPI.

**Developer:** Md. Mahabub Hossain  
**GitHub:** https://github.com/mahabub1993-prog  
**Repository:** https://github.com/mahabub1993-prog/Python-File-Organizer

---

## Project Overview

Python File Organizer helps users organize files quickly and efficiently without manually creating folders or moving files one by one.

The project currently includes:

- Desktop Application – Windows-based file organizer.
- Web Application – Browser-based file upload, automatic categorization, and ZIP download.

## Applications

### 1. Desktop Application

A Windows desktop application for automatically organizing files.

**Features**
- Automatic file organization.
- File categorization by extension.
- Separate folders for different file types.
- CSV organization report.
- Windows executable (`.exe`).
- Simple graphical user interface.

**Customer Delivery**

The ready-to-use Windows application is available in:

`Customer_Delivery/`

### 2. Smart File Organizer Web Application

A browser-based application developed using Python FastAPI.

**Features**
- Upload multiple files.
- Automatic file categorization.
- Organize uploaded files into separate folders.
- Download all organized files as a ZIP archive.
- Supports ZIP archives and multiple common file formats.
- Upload size limit: 100 MB per file.
- Browser-based interface.
- REST API documentation using Swagger UI.

**File Categories**

| Category | Examples |
|---|---|
| Documents | PDF, DOCX, TXT |
| Images | JPG, PNG, GIF |
| Spreadsheets | XLSX, CSV |
| Archives | ZIP, RAR, 7Z |
| Videos | MP4, AVI, MKV |
| Audio | MP3, WAV |
| Others | Other file types |

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming |
| FastAPI | Web backend |
| Uvicorn | ASGI server |
| Jinja2 | HTML templating |
| HTML | Web page structure |
| CSS | Web page styling |
| JavaScript | Frontend interactions |
| Pandas | CSV reporting |
| ZIP | Download organized files |
| Git & GitHub | Version control |

## Project Structure

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

- Python 3.10+
- Git
- Windows, Linux, or macOS

### Step 1: Clone Repository

```bash
git clone https://github.com/mahabub1993-prog/Python-File-Organizer.git
```

### Step 2: Open Web Application Folder

```bash
cd Python-File-Organizer/File_Organizer_Web
```

### Step 3: Create Virtual Environment

```bash
python -m venv venv
```

### Step 4: Activate Virtual Environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### Step 5: Install Requirements

```bash
pip install -r requirements.txt
```

### Step 6: Start Application

```bash
python -m uvicorn backend.main:app --reload
```

### Step 7: Open in Browser

Web Application:

http://127.0.0.1:8000

Swagger API Documentation:

http://127.0.0.1:8000/docs

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Web application homepage |
| GET | `/health` | Application health check |
| GET | `/info` | Application information |
| POST | `/upload` | Upload and organize files |
| GET | `/download-all` | Download organized files as ZIP |

## Testing

The Web Application has been tested locally with:

- Single-file uploads.
- Multiple-file uploads.
- Automatic file categorization.
- ZIP archive downloads.
- Large file upload testing (95 MB).
- Extracted ZIP content verification.

## Development Status

| Component | Status |
|---|---|
| Desktop Application | Completed |
| Web Application | Developed and locally tested |
| GitHub Repository | Published |
| Cloud Deployment | Planned |
| Future Automation Features | Planned |

## Future Improvements

- Cloud deployment.
- User authentication and accounts.
- Customer-specific file management.
- Cloud storage integration.
- Email and Google Drive automation.
- Advanced file processing features.

## Author

**Md. Mahabub Hossain**

Python Automation | AI Automation | Telecom Engineering

GitHub: https://github.com/mahabub1993-prog

LinkedIn: https://www.linkedin.com/in/md-mahabub-hossain-0846ab222

---

**Python File Organizer – Making File Management Simple and Automatic.**
