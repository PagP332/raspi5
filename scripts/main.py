import asyncio
import json
import datetime
import os
import logging
import utils

from realtime import AsyncRealtimeClient, RealtimeSubscribeStates

with open('scripts/supabase.json', 'r') as file:
    config = json.load(file)
url: str = config.get("SUPABASE_URL")
key: str = config.get("SUPABASE_SECRET")

logging.basicConfig(
    format="%(asctime)s:%(levelname)s - %(message)s", level=logging.INFO
)

def templateGenerate(payload):
    print("Recieved payload: ", payload)
    utils.templateGenerate()

def debugCapture(payload):
    print("Recieved payload: ", payload)
    utils.debugCapture()


async def test_postgres_changes(socket: AsyncRealtimeClient):
    await socket.connect()

    channel = socket.channel("test-postgres-changes")

    await channel.on_postgres_changes(
        "UPDATE", table="functions", filter='id=eq.1', callback=templateGenerate
    ).on_postgres_changes(
        "UPDATE", table="functions", filter='id=eq.2', callback=debugCapture
    ).subscribe()

    await socket.listen()



async def main():
    # Setup the broadcast socket and channel
    socket = AsyncRealtimeClient(f"{url}/realtime/v1", key, auto_reconnect=True)
    await socket.connect()

    await test_postgres_changes(socket)


asyncio.run(main())