
from fastapi import FastAPI, UploadFile, File, HTTPException, Request
from fastapi.responses import StreamingResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
from io import BytesIO
import uuid
import zipfile

# =====================================
# PROJECT CONFIGURATION
# =====================================

BASE_DIR = Path(__file__).resolve().parent.parent

UPLOAD_DIR = BASE_DIR / "uploads"
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

TEMPLATE_DIR = BASE_DIR / "templates"
templates = Jinja2Templates(directory=str(TEMPLATE_DIR))

# Maximum upload size: 100 MB per file
MAX_FILE_SIZE = 100 * 1024 * 1024

# Read file in 1 MB chunks
CHUNK_SIZE = 1024 * 1024

# =====================================
# FILE CATEGORIES
# =====================================

FILE_CATEGORIES = {
    "Documents": [
        ".pdf", ".doc", ".docx", ".txt",
        ".ppt", ".pptx", ".odt", ".rtf"
    ],

    "Images": [
        ".jpg", ".jpeg", ".png", ".gif",
        ".webp", ".bmp", ".svg"
    ],

    "Spreadsheets": [
        ".xlsx", ".xls", ".csv", ".ods"
    ],

    "Archives": [
        ".zip", ".rar", ".7z", ".tar", ".gz"
    ],

    "Videos": [
        ".mp4", ".avi", ".mov",
        ".mkv", ".wmv", ".webm"
    ],

    "Audio": [
        ".mp3", ".wav", ".aac",
        ".ogg", ".flac", ".m4a"
    ]
}

# Create category folders
for category in list(FILE_CATEGORIES.keys()) + ["Others"]:
    (UPLOAD_DIR / category).mkdir(
        parents=True,
        exist_ok=True
    )


# =====================================
# FASTAPI APPLICATION
# =====================================

app = FastAPI(
    title="Smart File Organizer",
    description="Upload, organize and download files.",
    version="2.1.0"
)


# =====================================
# CATEGORY DETECTION
# =====================================

def get_file_category(filename: str) -> str:

    extension = Path(filename).suffix.lower()

    for category, extensions in FILE_CATEGORIES.items():

        if extension in extensions:
            return category

    return "Others"


# =====================================
# UNIQUE FILE NAME
# =====================================

def get_unique_filename(filename: str) -> str:

    safe_name = Path(filename).name

    extension = Path(safe_name).suffix
    original_name = Path(safe_name).stem

    unique_id = uuid.uuid4().hex[:10]

    return f"{original_name}_{unique_id}{extension}"


# =====================================
# HOME PAGE
# =====================================

@app.get("/")
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )


# =====================================
# HEALTH CHECK
# =====================================

@app.get("/health")
async def health():

    return {
        "status": "healthy",
        "message": "Smart File Organizer is running"
    }


# =====================================
# API INFORMATION
# =====================================

@app.get("/info")
async def info():

    return {
        "application": "Smart File Organizer",
        "version": "2.1.0",
        "maximum_file_size": "100 MB per file",
        "upload_method": "Chunk-based",
        "categories": list(FILE_CATEGORIES.keys()) + ["Others"]
    }


# =====================================
# UPLOAD FILES
# =====================================

@app.post("/upload")
async def upload_files(
    files: list[UploadFile] = File(...)
):

    results = []

    for file in files:

        original_filename = Path(
            file.filename or "unnamed_file"
        ).name

        category = get_file_category(original_filename)

        category_dir = UPLOAD_DIR / category
        category_dir.mkdir(parents=True, exist_ok=True)

        unique_filename = get_unique_filename(
            original_filename
        )

        destination = category_dir / unique_filename

        total_size = 0

        try:

            with destination.open("wb") as output_file:

                while True:

                    chunk = await file.read(CHUNK_SIZE)

                    if not chunk:
                        break

                    total_size += len(chunk)

                    # Check 100 MB limit
                    if total_size > MAX_FILE_SIZE:

                        raise HTTPException(
                            status_code=413,
                            detail=(
                                f"{original_filename} exceeds "
                                "the 100 MB per-file limit."
                            )
                        )

                    output_file.write(chunk)

            results.append({
                "filename": original_filename,
                "saved_filename": unique_filename,
                "category": category,
                "size_bytes": total_size,
                "size_mb": round(
                    total_size / (1024 * 1024), 2
                ),
                "status": "uploaded and organized"
            })

        except HTTPException:

            destination.unlink(missing_ok=True)
            raise

        except Exception as error:

            destination.unlink(missing_ok=True)

            raise HTTPException(
                status_code=500,
                detail=f"Upload failed: {str(error)}"
            )

        finally:

            await file.close()

    return {
        "success": True,
        "message": "Files uploaded and organized successfully",
        "total_files": len(results),
        "maximum_file_size": "100 MB per file",
        "files": results
    }


# =====================================
# DOWNLOAD ALL FILES AS ZIP
# =====================================

@app.get("/download-all")
async def download_all_files():

    zip_buffer = BytesIO()

    total_files = 0

    try:

        with zipfile.ZipFile(
            zip_buffer,
            mode="w",
            compression=zipfile.ZIP_DEFLATED,
            allowZip64=True
        ) as zip_file:

            for category_dir in UPLOAD_DIR.iterdir():

                if not category_dir.is_dir():
                    continue

                for file_path in category_dir.rglob("*"):

                    if not file_path.is_file():
                        continue

                    archive_path = (
                        Path(category_dir.name)
                        / file_path.relative_to(category_dir)
                    )

                    zip_file.write(
                        file_path,
                        arcname=str(archive_path)
                    )

                    total_files += 1

        if total_files == 0:

            raise HTTPException(
                status_code=404,
                detail="No files available to download."
            )

        zip_buffer.seek(0)

        return StreamingResponse(
            zip_buffer,
            media_type="application/zip",
            headers={
                "Content-Disposition":
                'attachment; filename="Organized_Files.zip"'
            }
        )

    except HTTPException:
        raise

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=f"ZIP creation failed: {str(error)}"
        )


# =====================================
# CUSTOM OPENAPI FOR SWAGGER
# =====================================

def custom_openapi():

    if app.openapi_schema:
        return app.openapi_schema

    from fastapi.openapi.utils import get_openapi

    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes
    )

    def fix_schema(schema):

        if isinstance(schema, dict):

            schema.pop("contentMediaType", None)

            for value in schema.values():
                fix_schema(value)

        elif isinstance(schema, list):

            for item in schema:
                fix_schema(item)

    fix_schema(openapi_schema)

    app.openapi_schema = openapi_schema

    return app.openapi_schema


app.openapi = custom_openapi
