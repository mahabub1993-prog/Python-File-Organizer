
from pathlib import Path
from datetime import datetime
import shutil
import csv


# ==========================================
# 1. FILE CATEGORIES
# ==========================================

FILE_TYPES = {
    "PDF_Files": [".pdf"],

    "Images": [
        ".jpg", ".jpeg", ".png", ".gif",
        ".webp", ".bmp", ".tif", ".tiff"
    ],

    "Spreadsheets": [
        ".xlsx", ".xls", ".csv"
    ],

    "Documents": [
        ".doc", ".docx", ".txt", ".rtf", ".odt"
    ],

    "Videos": [
        ".mp4", ".mov", ".avi", ".mkv", ".webm"
    ],

    "Audio": [
        ".mp3", ".wav", ".m4a", ".aac",
        ".flac", ".ogg"
    ],

    "Compressed": [
        ".zip", ".rar", ".7z", ".tar", ".gz"
    ],

    "Programs": [
        ".exe", ".msi", ".bat", ".cmd"
    ],

    "Presentations": [
        ".ppt", ".pptx"
    ]
}


# ==========================================
# 2. GET FILE DESTINATION
# ==========================================

def get_destination(file_path: Path) -> str:
    """Identify file category using extension."""

    extension = file_path.suffix.lower()

    for folder_name, extensions in FILE_TYPES.items():

        if extension in extensions:
            return folder_name

    return "Others"


# ==========================================
# 3. AVOID DUPLICATE FILENAMES
# ==========================================

def unique_path(path: Path) -> Path:
    """Generate unique filename without overwriting."""

    if not path.exists():
        return path

    counter = 1

    while True:

        candidate = path.with_name(
            f"{path.stem}_{counter}{path.suffix}"
        )

        if not candidate.exists():
            return candidate

        counter += 1


# ==========================================
# 4. SCAN FILES RECURSIVELY
# ==========================================

def scan_files(source_folder: str):
    """Find files inside folder and all subfolders."""

    folder = Path(source_folder).resolve()

    if not folder.is_dir():
        raise NotADirectoryError(
            f"Folder not found: {folder}"
        )

    files = sorted(
        [
            file_path
            for file_path in folder.rglob("*")
            if file_path.is_file()
        ],
        key=lambda p: str(p).lower()
    )

    return folder, files


# ==========================================
# 5. PREVIEW FILES
# ==========================================

def preview_files(source_folder: str):
    """Preview files without moving them."""

    folder, files = scan_files(source_folder)

    results = []

    for file_path in files:

        category = get_destination(file_path)

        destination_folder = folder / category

        if file_path.parent == destination_folder:

            destination = file_path

            status = "Already Organized"

        else:

            destination = unique_path(
                destination_folder / file_path.name
            )

            status = "Preview"

        results.append({

            "filename": file_path.name,

            "source": str(
                file_path.relative_to(folder)
            ),

            "destination": str(
                destination.relative_to(folder)
            ),

            "category": category,

            "status": status
        })

    return results


# ==========================================
# 6. ORGANIZE FILES
# ==========================================

def organize_files(source_folder: str):
    """Move files into category folders safely."""

    folder, files = scan_files(source_folder)

    results = []

    for file_path in files:

        try:

            category = get_destination(file_path)

            destination_folder = folder / category

            # Skip already organized files
            if file_path.parent == destination_folder:

                results.append({

                    "filename": file_path.name,

                    "source": str(
                        file_path.relative_to(folder)
                    ),

                    "destination": str(
                        file_path.relative_to(folder)
                    ),

                    "category": category,

                    "status": "Already Organized"
                })

                continue

            # Create destination folder
            destination_folder.mkdir(
                parents=True,
                exist_ok=True
            )

            # Prevent overwriting
            destination = unique_path(
                destination_folder / file_path.name
            )

            # Move file
            shutil.move(
                str(file_path),
                str(destination)
            )

            results.append({

                "filename": file_path.name,

                "source": str(
                    file_path.relative_to(folder)
                ),

                "destination": str(
                    destination.relative_to(folder)
                ),

                "category": category,

                "status": "Moved"
            })

        except Exception as error:

            results.append({

                "filename": file_path.name,

                "source": str(file_path),

                "destination": "",

                "category": "Unknown",

                "status": f"Error: {error}"
            })

    return results


# ==========================================
# 7. GENERATE SUMMARY
# ==========================================

def get_summary(results):
    """Generate organization summary."""

    return {

        "total_files": len(results),

        "moved_files": sum(
            1 for item in results
            if item["status"] == "Moved"
        ),

        "preview_files": sum(
            1 for item in results
            if item["status"] == "Preview"
        ),

        "already_organized": sum(
            1 for item in results
            if item["status"] == "Already Organized"
        ),

        "errors": sum(
            1 for item in results
            if item["status"].startswith("Error:")
        )
    }


# ==========================================
# 8. EXPORT CSV REPORT
# ==========================================

def export_report(
    results,
    report_path="File_Organizer_Report.csv"
):
    """
    Export organization results to CSV.
    The CSV can be opened in Microsoft Excel.
    """

    report_file = Path(report_path)

    report_file.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    fieldnames = [
        "timestamp",
        "filename",
        "source",
        "destination",
        "category",
        "status"
    ]

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    with report_file.open(
        "w",
        newline="",
        encoding="utf-8-sig"
    ) as csv_file:

        writer = csv.DictWriter(
            csv_file,
            fieldnames=fieldnames
        )

        writer.writeheader()

        for item in results:

            writer.writerow({

                "timestamp": timestamp,

                "filename": item.get("filename", ""),

                "source": item.get("source", ""),

                "destination": item.get("destination", ""),

                "category": item.get("category", ""),

                "status": item.get("status", "")
            })

    return str(report_file.resolve())
