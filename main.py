from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from typing import List

app = FastAPI()

# 静的ファイルのサービングのための設定
app.mount("/templates", StaticFiles(directory="templates"), name="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_root():
    return FileResponse('templates/index.html')

@app.post("/upload/")
async def create_upload_files(files: List[UploadFile] = File(...), check_points: str = Form(...)):
    file_details = []
    for file in files:
        file_details.append({"filename": file.filename, "content_type": file.content_type})
    return {"message": "ファイルが受信されました", "files": file_details, "check_points": check_points}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
