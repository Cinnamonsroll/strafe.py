import asyncio
from client.Client import Client
from structure.Message import Message

async def main():
    client = Client()

    async def on_ready(c):
        print(c["user"]["username"])
        await client.user.set_presence({
            "status_text": "I like penis",
            "status": "online"
        })

    async def on_message(message: Message):
        if message.content == "]ping":
            await message.channel.send("test")

    client.on("ready", on_ready)
    client.on("messageCreate", on_message)

    await client.login("")

asyncio.run(main())