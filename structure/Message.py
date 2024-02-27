from client.types import MessageData
from structure.Channel import Channel

class Message(MessageData):
    def __init__(self, data: MessageData):
        self.room_type = data['room_type']
        self.space_id = data['space_id']
        self.channel = Channel({
            "client": data["client"],
            "id": data["room_id"]
        })
        self.content = data['content']
        self.message_reference_id = data['message_reference_id']
        self.id = data['id']
        self.created_at = data['created_at']
        self.author = data['author']
