from fastapi import APIRouter, File, UploadFile
from models import Image


image_router = APIRouter(
    prefix = '/image',
    tags = ['image']
)

@image_router.post("/upload")
async def upload(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        file_location = f"files/{file.filename}"
        with open(file.filename, 'wb') as f:
            f.write(contents)
    except Exception:
        return {"There was an error uploading the file"}
    finally:
        await file.close()
        
    return {f"Successfuly uploaded {file.filename}"}
