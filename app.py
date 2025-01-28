import pyttsx3
from fastapi import FastAPI
from io import BytesIO

app = FastAPI()

engine = pyttsx3.init()

@app.post("/synthesize/")
async def synthesize(text: str):
    try:
        # pyttsx3で音声合成
        audio_fp = BytesIO()
        engine.save_to_file(text, audio_fp)
        audio_fp.seek(0)
        
        # 音声ファイルをBase64エンコードして返す
        audio_base64 = base64.b64encode(audio_fp.read()).decode('utf-8')
        return {"audio": audio_base64}
    except Exception as e:
        return {"error": str(e)}

# 起動方法
# uvicorn app:app --reload
