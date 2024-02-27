import asyncio
import json
import websockets
from client.types import Events
from config import OpCodes
from structure.ClientUser import ClientUser
from structure.Message import Message

class WebsocketClient:
    def __init__(self, client):
        self.client = client
        self.gateway = None
        self.ws = None
        self.heartbeat_interval = None

    async def connect(self):
        if not self.gateway:
            try:
                async with websockets.connect(f"{self.client.config['ws']}") as ws:
                    response = await ws.recv()
                    data = json.loads(response)
                    self.gateway = self.client.config['ws']
            except Exception as e:
                await self.client.emit("error", "Looks like the Strafe API is down. Please try reconnecting later.")
                raise Exception(f"Looks like {self.client.config['ws']} might be down!")

        self.ws = await websockets.connect(self.gateway)

        await self.ws.send(json.dumps({"op": OpCodes["IDENTIFY"], "data": {"token": self.client.token}}))

        async for message in self.ws:
            data = json.loads(message)
            op = data.get('op')
            event = data.get('event')
            payload = data.get('data')

            if op == OpCodes["HELLO"]:
                heartbeat_interval = payload['heartbeat_interval']
                await self.start_heartbeat(heartbeat_interval)  # Await start_heartbeat
            elif op == OpCodes["DISPATCH"]:
                if event == "READY":
  
                    self.client.user = ClientUser({
                        **payload["user"],
                        "client": self.client
                    })
                    await self.client.emit("ready", payload)
                elif event == "PRESENCE_UPDATE":
                    if self.client.user and self.client.user.id == payload['user']['id']:
                        self.client.user.presence = payload['presence']
                    await self.client.emit("presenceUpdate", payload)
                elif event == "MESSAGE_CREATE":
                    message = Message({
                        **payload,
                        "client": self.client
                    })
                    await self.client.emit("messageCreate", message)

    async def send(self, op, data: dict):
        await self.ws.send(json.dumps({"op": op, "data": data}))

    async def close(self):
        await self.stop_heartbeat()
        await self.ws.close()

    async def stop_heartbeat(self):
        if self.heartbeat_interval:
            self.heartbeat_interval.cancel()

    async def start_heartbeat(self, interval):
        async def heartbeat():
            while True:
                await asyncio.sleep(interval / 1000)
                await self.send(OpCodes["HEARTBEAT"], {})

        self.heartbeat_interval = asyncio.create_task(heartbeat())

    async def reconnect(self):
        await self.stop_heartbeat()
        await self.ws.close()
        await asyncio.sleep(5)
        await self.connect()
