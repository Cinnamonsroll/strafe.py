import asyncio
from client.WebsocketClient import WebsocketClient
from client.types import ClientOptions
from config import API, CDN, WS
from structure import ClientUser



class EventEmitter:
    def __init__(self):
        self._listeners = {}

    def on(self, event, callback):
        if event not in self._listeners:
            self._listeners[event] = []
        self._listeners[event].append(callback)

    async def emit(self, event, *args, **kwargs):
        if event in self._listeners:
            for listener in self._listeners[event]:
                await listener(*args, **kwargs)

class Client(EventEmitter):
    def __init__(self, options: ClientOptions = None):
        super().__init__()
        self.config = {
            "equinox": API,
            "nebula": CDN,
            "ws": WS
        }
        self.token = None  # type: str
        self.user = None  # type: ClientUser
        self.ws = WebsocketClient(self)

    async def login(self, token: str):
        self.token = token
        await self.ws.connect()
