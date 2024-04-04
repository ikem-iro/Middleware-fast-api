from fastapi import APIRouter, UploadFile, File
from controllers.upload_controller import process_files



router = APIRouter(prefix="/api", tags=["Upload"])


@router.post('/upload')
async def upload_file(files: list[UploadFile] = File(default=None, title="File", description="File to upload")):
    """
    A function to upload files. Takes a list of UploadFile objects as input and processes them.
    
    Parameters:
        files (list[UploadFile]): File or files to upload.
    
    Returns:
        dict: A message containing the processed data.
    """

    data = process_files(files)

    return {"message": data}