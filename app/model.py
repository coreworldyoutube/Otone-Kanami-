import torch
import requests
from io import BytesIO

def download_model_from_google_drive(drive_url):
    # Google Driveからモデルをダウンロード
    file_id = drive_url.split('/')[-2]
    url = f'https://drive.google.com/uc?export=download&id={file_id}'
    response = requests.get(url)
    return BytesIO(response.content)

# モデルファイルをGoogle Driveからダウンロード
model_file = download_model_from_google_drive('https://drive.google.com/file/d/your_file_id/view?usp=sharing')

# Tacotron2のモデルを読み込む
model = torch.load(model_file)
model.eval()
