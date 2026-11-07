
from pathlib import Path
import shutil

# Only organize files inside this test folder
SOURCE_FOLDER = Path.home() / "Desktop" / "FileOrganizer_Test"


DRY_RUN = True

FILE_TYPES = {
    "PDF_Files": [".pdf"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Spreadsheets": [".xlsx", ".xls", ".csv"],
    "Documents": [".doc", ".docx", ".txt", ".rtf"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Audio": [".mp3", ".wav", ".m4a"],
}

def get_destination(file):
    extension = file.suffix.lower()

    for folder_name, extensions in FILE_TYPES.items():
        if extension in extensions:
            return folder_name

    return "Others"


def unique_path(path):
    """Avoid overwriting an existing file."""
    if not path.exists():
        return path

    counter = 1

    while True:
        new_path = path.with_name(
            f"{path.stem}_{counter}{path.suffix}"
        )

        if not new_path.exists():
            return new_path

        counter += 1


def organize_files():
    if not SOURCE_FOLDER.is_dir():
        print(f"Folder not found: {SOURCE_FOLDER}")
        return

    files = [
        item for item in SOURCE_FOLDER.iterdir()
        if item.is_file()
    ]

    if not files:
        print("No files found in the test folder.")
        return

    for file in files:
        folder_name = get_destination(file)
        destination_folder = SOURCE_FOLDER / folder_name
        destination = unique_path(destination_folder / file.name)

        if DRY_RUN:
            print(f"[PREVIEW] {file.name} -> {folder_name}/")
        else:
            destination_folder.mkdir(exist_ok=True)
            shutil.move(str(file), str(destination))
            print(f"[MOVED] {file.name} -> {folder_name}/")

    if DRY_RUN:
        print("\nPreview finished. No files were moved.")
        print("Check the results, then set DRY_RUN = False.")
    else:
        print("\nFile organization completed!")


if __name__ == "__main__":
    organize_files()

