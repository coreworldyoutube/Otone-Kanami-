from fastapi import FastAPI
from gtts import gTTS
from io import BytesIO
import base64

app = FastAPI()

@app.post("/synthesize/")
async def synthesize(text: str):
    tts = gTTS(text=text, lang='ja')
    audio_fp = BytesIO()
    tts.save(audio_fp)
    audio_fp.seek(0)
    audio_base64 = base64.b64encode(audio_fp.read()).decode('utf-8')
    return {"audio": audio_base64}
