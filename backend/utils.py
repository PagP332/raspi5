import json
from PIL import Image
from supabase import create_client, Client
import readWrite as rw
from datetime import datetime

# Load URL and Key from JSON file
with open('../backend/supabase.json', 'r') as file:
    config = json.load(file)
url: str = config.get("SUPABASE_URL")
key: str = config.get("SUPABASE_SECRET")
supabase: Client = create_client(url, key)

def pushAlert(image: str):
    time = datetime.now().strftime('%Y%m-%d%H-%M%S')
    uid = f"alert_{time}" # Generate Unique Identifier of Alert based on the datetime it is created
    imagePath = f"public/alert_{uid}"
    resp = supabase.storage.from_("AlertImages").upload(path=imagePath, file=image, file_options={"cache-control": "3600", "upsert": "false", "content-type":"image/jpeg"})
    rw.write(supabase=supabase, table="Alerts", uid=uid, is_resolved=False, image_path=imagePath)
    print(resp)

pushAlert("../6143325340081178130.jpg")
