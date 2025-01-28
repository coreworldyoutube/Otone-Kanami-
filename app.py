from fastapi import FastAPI
import torch
from model import Tacotron2 # 訓練したモデルのインポート
from gtts import gTTS
import io
import base64

# FastAPIのインスタンス
app = FastAPI()

# 訓練したモデルを読み込み
model = Tacotron2()
model.load_state_dict(torch.load('model.pth'))

@app.post("/synthesize/")
async def synthesize_text(text: str):
    # テキストを音声に変換
    audio = model.synthesize(text)  # モデルを使って音声を生成
    audio_base64 = base64.b64encode(audio).decode('utf-8')  # Base64エンコードして返す

    return {"audio": audio_base64}
