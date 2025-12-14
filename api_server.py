from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import shutil, os, uuid

app = FastAPI(title="BananaSlides")

@app.post("/generate")
def generate_ppt(upload: UploadFile = File(...)):
    uid = uuid.uuid4().hex
    in_path  = f"/tmp/{uid}_{upload.filename}"
    out_path = f"/tmp/{uid}.pptx"
    with open(in_path, "wb") as f:
        shutil.copyfileobj(upload.file, f)
    # ===== 这里调你已有的 services =====
    # 伪代码：services.process(in_path, out_path)
    # ===================================
    return FileResponse(out_path, filename="banana_slides.pptx")
