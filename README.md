\# File Organizer – Automated File Management System



A Python-based file management automation project designed to organize files efficiently through a Windows desktop application, with planned web and cloud automation extensions.



\*\*Current Release:\*\* Desktop Application v1.0  

\*\*Development Status:\*\* Desktop Version Completed | Web \& Cloud Versions Planned



\---



\## 1. Project Overview



File Organizer helps users organize files automatically according to their file extensions.



Instead of manually sorting files, users can select a folder, preview the organization plan, and move files into categorized folders through a graphical user interface.



The project is designed with a reusable Python core engine so that future web and cloud applications can use the same file organization logic.



\## 2. Application Editions



\### A. Windows Desktop Application



\*\*Status: Implemented – Version 1.0\*\*



The current Windows desktop application includes:



\- Graphical User Interface (GUI)

\- Folder selection

\- Recursive file scanning

\- File preview before organization

\- Automatic file categorization

\- Duplicate filename protection

\- CSV report generation

\- Confirmation before moving files



\*\*How it works:\*\*



1\. Open `FileOrganizer.exe`.

2\. Select a source folder.

3\. Click `Preview Files`.

4\. Review the file organization plan.

5\. Click `Organize Files`.

6\. Export the operation report as CSV.



\### B. Web Application



\*\*Status: Planned – Future Development\*\*



The planned web version will allow users to:



\- Upload files through a browser.

\- Preview file categories.

\- Organize uploaded files.

\- Download organized files as a ZIP package.

\- View processing summaries.



Planned technology:

\- Python

\- FastAPI

\- HTML, CSS and JavaScript

\- ZIP file processing



These features are not yet implemented.



\### C. Cloud Automation



\*\*Status: Planned – Future Development\*\*



The planned cloud version will focus on automated file management using cloud storage services.



Potential features:



\- Google Drive integration

\- Authorized cloud folder access

\- Automatic file categorization

\- Cloud-based organization workflows

\- Processing reports



Cloud access will require user authorization and appropriate permissions. These features are not yet implemented.



\---



\## 3. Supported File Categories



The current desktop version supports the following categories:



| Category | Description |

|---|---|

| PDF\_Files | PDF documents |

| Images | JPG, PNG and other supported images |

| Spreadsheets | CSV, XLSX and related files |

| Documents | TXT, DOCX and related files |

| Videos | Video files |

| Audio | Audio files |

| Compressed | ZIP and archive files |

| Programs | Executable and installer files |

| Presentations | PowerPoint files |

| Others | Other supported file extensions |



Actual categorization depends on the extensions configured in the application.



\## 4. Project Architecture



```text

Python\_Automation\_Project/

│

├── core/

│   ├── \_\_init\_\_.py

│   └── organizer.py

│

├── file\_organizer.py

├── file\_organizer\_gui.py

├── FileOrganizer.spec

├── Customer\_Delivery/

│   ├── FileOrganizer.exe

│   ├── README.txt

│   └── User\_Guide.txt

│

├── .gitignore

└── README.md

```



The `core/organizer.py` module contains the shared file organization logic.



The desktop GUI uses this core engine to preview, organize and report file operations.



\## 5. Key Features



\- Automatic file organization

\- File extension-based categorization

\- Recursive folder scanning

\- Preview before moving files

\- Duplicate filename handling

\- CSV operation reports

\- User-friendly desktop interface

\- Reusable core architecture



\## 6. Technology Stack



| Technology | Purpose |

|---|---|

| Python | Core programming |

| Tkinter | Desktop GUI |

| CSV | Report generation |

| PyInstaller | Windows executable packaging |

| FastAPI | Planned web backend |

| Google Drive API | Planned cloud integration |



\## 7. Installation and Usage



\### Windows Desktop Version



1\. Download `FileOrganizer.exe` or the ZIP release.

2\. Extract the ZIP package if downloaded.

3\. Open `FileOrganizer.exe`.

4\. Select a test folder.

5\. Preview the files.

6\. Organize the files.

7\. Export the CSV report.



\### Run from Python Source



Clone the repository:



```bash

git clone YOUR\_GITHUB\_REPOSITORY\_URL

cd Python\_Automation\_Project

```



Create a virtual environment:



```bash

python -m venv venv

```



Activate it on Windows PowerShell:



```powershell

.\\venv\\Scripts\\Activate.ps1

```



Install required dependencies:



```bash

pip install pandas pyinstaller

```



Run the desktop GUI:



```bash

python file\_organizer\_gui.py

```



Note: Additional dependencies may be required as the project evolves. The standalone EXE is intended to bundle its Python runtime; compatibility on other PCs still requires testing.



\## 8. Safety and Data Handling



\- Always test using sample files first.

\- Keep backups of important files.

\- Review the preview before organizing.

\- Confirm before moving files.

\- Avoid running the application on important folders without testing.



The desktop version moves files rather than deleting them. Users should still maintain backups.



\## 9. Current Testing Status



The following have been tested locally:



\- Desktop GUI launch

\- Windows EXE launch

\- File organization workflow

\- Duplicate filename handling

\- CSV report export

\- Customer delivery ZIP creation and extraction



Cross-PC compatibility has not yet been independently verified.



Web and cloud applications have not yet been implemented or tested.



\## 10. Development Roadmap



\- \[x] Shared Python file organization engine

\- \[x] Windows desktop GUI

\- \[x] Standalone EXE build

\- \[x] CSV report export

\- \[x] Customer documentation

\- \[x] Desktop delivery ZIP

\- \[ ] Web application using FastAPI

\- \[ ] Browser upload and ZIP download

\- \[ ] Google Drive integration

\- \[ ] Cloud automation workflows

\- \[ ] Automated testing and deployment



\## 11. License



License: To be determined.



Commercial use, redistribution and modification terms will be specified when a project license is selected.



\## 12. Project Purpose



This project demonstrates practical Python automation, desktop application development, file processing, GUI design and software packaging.



The long-term goal is to develop a unified file management solution for desktop, web and cloud environments.



\---



\*\*Project:\*\* File Organizer  

\*\*Version:\*\* 1.0  

\*\*Primary Language:\*\* Python  

\*\*Current Platform:\*\* Windows Desktop



