from client import Client
from typing import Optional, Dict
class ClientConfig:
    def __init__(self, equinox: str, nebula: str):
        self.equinox = equinox
        self.nebula = nebula

class ClientOptions:
    def __init__(self, config: ClientConfig = None):
        self.config = config

class UserPresence:
    def __init__(self, online: bool, status: str, status_text: str):
        self.online = online
        self.status = status
        self.status_text = status_text

class ClientUserEditOptions:
    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email

Events = str

class IUser:
    def __init__(self, client: Client, id: str, accent_color: int, avatar: str, avatar_decoration: str, banned: bool,
                 banner: str, bot: bool, created_at: int, discriminator: int, email: str, edited_at: int, flags: int,
                 global_name: str, locale: str, phone_number: str, premium_type: int, presence: UserPresence,
                 public_flags: int, system: bool, username: str, verified: bool):
        self.client = client
        self.id = id
        self.accent_color = accent_color
        self.avatar = avatar
        self.avatar_decoration = avatar_decoration
        self.banned = banned
        self.banner = banner
        self.bot = bot
        self.created_at = created_at
        self.discriminator = discriminator
        self.email = email
        self.edited_at = edited_at
        self.flags = flags
        self.global_name = global_name
        self.locale = locale
        self.phone_number = phone_number
        self.premium_type = premium_type
        self.presence = presence
        self.public_flags = public_flags
        self.system = system
        self.username = username
        self.verified = verified




class Author:
    id: str
    username: str
    discriminator: int
    global_name: str
    display_name: str
    avatar: str
    bot: bool
    presence: Dict[str, Optional[str]]

class MessageData:
    room_type: int
    space_id: str
    room_id: str
    content: str
    message_reference_id: Optional[str]
    id: str
    created_at: int
    author: Author
    client: Client
