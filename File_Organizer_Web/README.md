# Smart File Organizer Web

A FastAPI-based web application that automatically organizes uploaded files into categories.

## Features

- Multiple file upload
- Automatic file categorization
- 100 MB maximum size per file
- Upload progress indicator
- Download all organized files as ZIP
- Simple web interface

## Supported Categories

- Documents
- Images
- Spreadsheets
- Archives
- Videos
- Audio
- Others

## Technology Stack

- Python
- FastAPI
- Uvicorn
- Jinja2
- HTML, CSS, JavaScript

## Installation

1. Clone the repository.
2. Open the project folder:

   cd File_Organizer_Web

3. Create a virtual environment:

   python -m venv venv

4. Activate it:

   .\venv\Scripts\Activate.ps1

5. Install dependencies:

   pip install -r requirements.txt

6. Start the application:

   python -m uvicorn backend.main:app --reload

7. Open in browser:

   http://127.0.0.1:8000

## API Documentation

http://127.0.0.1:8000/docs

## Author

Md. Mahabub Hossain
