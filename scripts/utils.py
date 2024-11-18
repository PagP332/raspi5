import json
from PIL import Image
from supabase import create_client, Client
import readWrite as rw
from datetime import datetime
import time
from datetime import datetime, timezone, timedelta

# from capture import capture

# Load URL and Key from JSON file
with open('scripts/supabase.json', 'r') as file:
    config = json.load(file)
url: str = config.get("SUPABASE_URL")
key: str = config.get("SUPABASE_SECRET")
supabase: Client = create_client(url, key)

def pushAlert(image: str):
    time = datetime.now().strftime('%Y%m-%d%H-%M%S')
    uid = f"alert_{time}" # Generate Unique Identifier of Alert based on the datetime it is created
    imagePath = f"public/alert_{uid}"
    rw.write(supabase=supabase, table="Alerts", uid=uid, is_resolved=False, image_path=imagePath)
    resp = supabase.storage.from_("AlertImages").upload(path=imagePath, file=image, file_options={"cache-control": "3600", "upsert": "false", "content-type":"image/jpeg"})
    print(resp)

from picamera2 import Picamera2
import io
import time

picam2 = Picamera2()
def capture():
    capture_config = picam2.create_still_configuration()
    picam2.configure(capture_config)
    picam2.start()
    time.sleep(1)
    data = io.BytesIO()
    picam2.capture_file(data, format='jpeg')
    return data

def updateHandshake():
    # Generate the current time in the desired format
    response = supabase.table("handshake").select("*").eq("id", 1).execute().json()
    print(response)

    timestamp = datetime.fromisoformat(last_time)
    current_time = datetime.now(timezone.utc)

    elapsed_time = current_time - timestamp

    if elapsed_time >= timedelta(minutes=1):
        current_time = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S.%f+00")
        response = supabase.table("handshake").update({"last_time": current_time}).eq("id",1).execute()
        print("Handshake prompt")


def templateGenerate():
    image = capture().getvalue()
    picam2.stop()
    imagePath = f"template/template"
    # rw.write(supabase=supabase, table="Alerts", uid=uid, is_resolved=False, image_path=imagePath)
    resp = supabase.storage.from_("AlertImages").upload(path=imagePath, file=image, file_options={"cache-control": "3600", "upsert": "true", "content-type":"image/jpeg"})
    print(resp)

def debugCapture():
    pushAlert(capture().getvalue())
    picam2.stop()
