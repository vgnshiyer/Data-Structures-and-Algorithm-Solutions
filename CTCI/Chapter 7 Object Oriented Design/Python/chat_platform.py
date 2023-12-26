from dataclasses import dataclass
from typing import List, Set

@dataclass
class ChatServer:
    users: dict = {}
    chats: dict = {}

    def add_user(self, user: User):
        pass

    def get_user(self, user_id: int):
        pass

    def update_user(self, user_id: User, user: User):
        pass

    def remove_user(self, user_id: int):
        pass

@dataclass
class Chat:
    id_: int
    chat_id = 0
    history: list = []

    def __post_init__(self):
        Chat.chat_id += 1
        self.id_ = Chat.chat_id

@dataclass
class ChatGroup(Chat):
    members: set = set()

@dataclass
class PrivateChat(Chat):
    member1: User = None
    member2: User = None

@dataclass
class User:
    id_: int
    name: str
    age: int

    chat_server: ChatServer
    
    friends: set = set()
    friend_invitations: list = []

    chats: set = set()
    chat_invitations: set = set()

    def create_chat_group(self):
        chat_group = ChatGroup()
        chat_group.add(self.id_)
        self.chats.add(chat_group.id_)

    def create_private_chat(self):
        pvt_chat = PrivateChat()
        pvt_chat.add(self.id_)
        self.chats.add(pvt_chat.id_)
        
    def send_friend_request(self, user_id: int):
        pass

    def notify_friend_requests(self, user_id: int):
        self.friend_invitations.add(user_id)

    def accept_friend_request(self, user_id: int):
        pass

    def reject_friend_request(self, user_id: int):
        pass
    
    def invite_user_to_chat(self, user_id: int, chat_id: int):
        pass

    def notify_chat_join_request(self, user_id: int, chat_id: int):
        pass

    def accept_chat_join_requests(self, chat_id: int):
        pass

    def reject_chat_join_requests(self, chat_id: int):
        pass

    def send_message(self, msg: str, chat_id: int):
        pass

    def message_notification(self, msg: str, user_id: int, chat_id: int):
        pass