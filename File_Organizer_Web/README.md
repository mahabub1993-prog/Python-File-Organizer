# Smart File Organizer — Web Application

A browser-based file management application built with **Python and FastAPI**. It automatically categorizes uploaded files, organizes them into folders, and allows users to download all organized files in a ZIP archive.

## Features

- Upload single or multiple files.
- Automatically categorize files by extension.
- Organize files into category-based folders.
- Download all organized files as a ZIP archive.
- Upload progress indicator.
- Simple, browser-based user interface.
- REST API with interactive Swagger documentation.
- Maximum configured file size: **100 MB per file**.

## Supported File Categories

| Category | Example File Types |
|---|---|
| Documents | PDF, DOC, DOCX, TXT |
| Images | JPG, JPEG, PNG, GIF |
| Spreadsheets | XLS, XLSX, CSV |
| Archives | ZIP, RAR, 7Z |
| Videos | MP4, AVI, MKV |
| Audio | MP3, WAV |
| Others | Other supported file extensions |

## Technology Stack

- **Backend:** Python, FastAPI
- **ASGI Server:** Uvicorn
- **Template Engine:** Jinja2
- **Frontend:** HTML, CSS, JavaScript
- **File Processing:** Python Standard Library
- **API Documentation:** Swagger UI / OpenAPI

## Project Structure

```text
File_Organizer_Web/
│
├── backend/
│   └── main.py
│
├── templates/
│   └── index.html
│
├── static/
│
├── tests/
│
├── uploads/
│   ├── Documents/
│   ├── Images/
│   ├── Spreadsheets/
│   ├── Archives/
│   ├── Videos/
│   ├── Audio/
│   └── Others/
│
├── .gitignore
├── requirements.txt
└── README.md
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/mahabub1993-prog/Python-File-Organizer.git
```

### 2. Open the Web Application Directory

```bash
cd Python-File-Organizer/File_Organizer_Web
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Start the Application

```bash
python -m uvicorn backend.main:app --reload
```

### 7. Open in Browser

Web Application:

http://127.0.0.1:8000

Swagger API Documentation:

http://127.0.0.1:8000/docs

Alternative API Documentation:

http://127.0.0.1:8000/redoc

## API Endpoints

| Endpoint | Method | Description |
|---|---|---|
| `/` | GET | Web application interface |
| `/health` | GET | Application health check |
| `/info` | GET | Application information |
| `/upload` | POST | Upload and organize files |
| `/download-all` | GET | Download organized files as ZIP |

## File Upload Workflow

1. Open the Web Application in a browser.
2. Select one or multiple files.
3. Upload the selected files.
4. The application categorizes the files automatically.
5. Organized files are stored in their respective category folders.
6. Download the organized files together as a ZIP archive.

## Deployment

The application is designed to support deployment on cloud hosting platforms such as Render.

**Render Configuration:**

- Runtime: Python 3
- Root Directory: `File_Organizer_Web`
- Build Command:

```bash
pip install -r requirements.txt
```

- Start Command:

```bash
uvicorn backend.main:app --host 0.0.0.0 --port $PORT
```

**Deployment Status:** Cloud deployment configuration documented; live deployment pending.

**Important:** The default Render filesystem is ephemeral. Uploaded files may not persist after a service restart or redeployment. Persistent storage is required if uploaded files must be retained.

## Security and Limitations

- Maximum configured upload size is 100 MB per file.
- Only supported file extensions are categorized.
- Uploaded files should be treated as untrusted input.
- Production deployment should include appropriate file validation, storage management, and security controls.

## Author

**Md. Mahabub Hossain**

GitHub: https://github.com/mahabub1993-prog

LinkedIn: https://www.linkedin.com/in/md-mahabub-hossain-0846ab222

## License

This project is maintained as a Python automation and file management development project.
