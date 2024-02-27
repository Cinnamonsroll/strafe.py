
import aiohttp


class Channel():
    def __init__(self, data):
        self.client = data["client"]
        self.id = data["id"]
    
    async def send(self, content: str):
        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"https://equinox.strafechat.dev/v1/rooms/{self.id}/messages",
                headers={"Authorization": self.client.token},
                json={"channel": self.id, "content": content}
            ) as response:

                if response.status == 200:
                    return await response.json()
                else:
                    raise ValueError(await response.json())
