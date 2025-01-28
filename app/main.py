from fastapi import FastAPI
from model import synthesize_text
from pydantic import BaseModel
import io
import base64
from fastapi.responses import JSONResponse

app = FastAPI()

class TextRequest(BaseModel):
    text: str

@app.post("/synthesize/")
async def synthesize(request: TextRequest):
    # モデルを使ってテキストから音声を生成
    audio_data = synthesize_text(request.text)
    
    # 音声データをBase64エンコード
    audio_base64 = base64.b64encode(audio_data).decode('utf-8')

    # Base64音声データを返す
    return JSONResponse(content={"audio": audio_base64})
