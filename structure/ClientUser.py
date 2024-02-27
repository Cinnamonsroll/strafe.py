import aiohttp
import json
from client.types import IUser
from config import OpCodes 
from typing import Dict, Any, Union

from structure.User import User


class ClientUser(User):
    def __init__(self, data: 'IUser'):
        super().__init__(data)


    async def set_presence(self, presence: Dict[str, Any]):
        await self.client.ws.send(OpCodes["PRESENCE"], presence)

    async def edit(self, data: Dict[str, Union[str, int]]):
        headers = {
            "Content-Type": "application/json",
            "Authorization": self.client.token
        }
        async with aiohttp.ClientSession() as session:
            async with session.patch(f"{self.client.config.equinox}/users/@me", headers=headers, json=data) as response:
                res_data = await response.json()
                username = res_data.get("username")
                discriminator = res_data.get("discriminator")
                if not response.ok:
                    raise Exception("Failed to edit user: " + res_data.get("message", ""))
                self.username = username or self.username
                self.discriminator = discriminator or self.discriminator
