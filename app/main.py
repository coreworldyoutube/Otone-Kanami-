from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from model import synthesize_text
from pydantic import BaseModel
import base64
from fastapi.responses import JSONResponse

# FastAPIのインスタンスを作成
app = FastAPI()

# 静的ファイル（HTML, CSS, JSなど）を提供する
app.mount("/static", StaticFiles(directory="app/static"), name="static")

class TextRequest(BaseModel):
    text: str

# /synthesize エンドポイントを作成
@app.post("/synthesize/")
async def synthesize(request: TextRequest):
    # テキストから音声を生成
    audio_data = synthesize_text(request.text)
    
    # 音声データをBase64エンコードして返す
    audio_base64 = base64.b64encode(audio_data).decode('utf-8')
    return JSONResponse(content={"audio": audio_base64})

# 最初にアクセスしたときにvoice_synthesizer.htmlを返す
@app.get("/", response_class=HTMLResponse)
async def get_homepage():
    return HTMLResponse(content=open("app/static/voice_synthesizer.html").read())
