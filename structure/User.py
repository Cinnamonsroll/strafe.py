from typing import Optional
from client import Client
from client.types import IUser, UserPresence 

class User(IUser):
    def __init__(self, data: IUser):
        self.id: str = data["id"]
        self.accent_color: Optional[int] = data["accent_color"]
        self.avatar: Optional[str] = data["avatar"]
        self.avatar_decoration: Optional[str] = data["avatar_decoration"]
        self.banner: Optional[str] = data["banner"]
        self.bot: bool = data["bot"]
        self.client: Client = data["client"]
        self.created_at: int = data["created_at"]
        self.discriminator: int = data["discriminator"]
        self.edited_at: int = data["edited_at"]
        self.flags: int = data["flags"]
        self.global_name: str = data["global_name"]
        self.locale: Optional[str] = data["locale"]
        self.premium_type: int = data["premium_type"]
        self.presence: UserPresence = data["presence"]
        self.public_flags: int = data["public_flags"]
        self.system: bool = data["system"]
        self.username: str = data["username"]
        self.verified: bool = data["verified"]
