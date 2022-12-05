from fastapi import FastAPI, UploadFile, File
from tensorflow.io import decode_jpeg

app = FastAPI()

@app.post("/image")
async def post_image(file: UploadFile = File(...)):
    contents = await file.read()
    img = decode_jpeg(contents)
    print(img.shape)
    return {"idxs": [1,2,3,4,5]}
