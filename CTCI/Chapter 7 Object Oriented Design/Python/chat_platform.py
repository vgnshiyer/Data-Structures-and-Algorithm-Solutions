from dataclasses import dataclass
from typing import List, Set
from functools import wraps

@dataclass
class ChatPlatform:
    users = {}
    chats = {}

    def add_user(self, user):
        self.users[user.id_] = user

    def get_user(self, user_id: int):
        if user_id in self.users:
            return self.users[user_id]
        raise UserNotFoundException

    def update_user(self, user_id, user):
        if user_id in self.users:
            self.users[user_id] = user
        raise UserNotFoundException

    def remove_user(self, user_id: int):
        if user_id in self.users:
            del self.users[user_id]
        raise UserNotFoundException

    def add_chat(self, chat):
        self.chats[chat.id_] = chat

    def get_chat(self, chat_id: int):
        if chat_id in self.chats:
            return self.chats[chat_id]
        raise ChatNotFoundException

    def remove_chat(self, chat_id: int):
        if chat_id in self.chats:
            del self.chats[chat_id]
        raise ChatNotFoundException

@lambda coro: wraps(coro)(lambda *a, **kw: [ci := coro(*a, **kw), next(ci)][0])
def server(members):
    while True:
        (sender, chat_id, msg) = (yield)
        if not msg: continue
        for member in members:
            member.message_notification(msg, sender, chat_id)

class Chat:
    current_chat_id = 0
    history = []
    members = set()

    def __init__(self):
        Chat.current_chat_id += 1
        self.id_ = Chat.current_chat_id

    def add_member(self, member_id: int):
        self.members.add(member_id)

    def send_message(self, sender_id: int, msg: str):
        self.history.append(msg)
        self.server.send(
            (sender_id, self.id_, msg)
        )

class ChatGroup(Chat):
    pass

class PrivateChat(Chat):
    pass

@dataclass
class User:
    id_: int
    name: str
    age: int

    chat_platform: ChatPlatform
    
    friends = set()
    friend_invitations = []

    chats = set()
    chat_invitations = set()

    current_user_id = 0

    def __post_init__(self):
        User.current_user_id += 1
        self.id_ = User.current_user_id

    def create_chat_group(self):
        chat_group = ChatGroup()
        chat_group.add_member(self.id_)
        self.chats.add(chat_group.id_)
        self.chat_platform.add_chat(chat_group)

    def create_private_chat(self):
        pvt_chat = PrivateChat()
        pvt_chat.add_member(self.id_)
        self.chats.add(pvt_chat.id_)
        self.chat_platform.add_chat(chat_group)
        
    def send_friend_request(self, to_id: int):
        if to_id in self.friends:
            raise AlreadyAFriendException
        user = self.chat_platform.get_user(to_id)
        user.notify_friend_requests(self.id_)

    def notify_friend_requests(self, from_id: int):
        self.friend_invitations.add(from_id)

    def accept_friend_request(self, from_id: int):
        if from_id not in self.friend_invitations:
            raise NoFriendRequestFromUserException
        self.friends.add(from_id)
        self.friend_invitations.remove(from_id)

    def reject_friend_request(self, from_id: int):
        if from_id not in self.friend_invitations:
            raise NoFriendRequestFromUserException
        self.friend_invitations.remove(from_id)
    
    def invite_user_to_chat(self, to_id: int, chat_id: int):
        if chat_id not in self.chats:
            raise ChatNotFoundException
        user = self.chat_platform.get(to_id)
        user.notify_chat_join_request(self.id_, chat_id)

    def notify_chat_join_request(self, from_id: int, chat_id: int):
        self.chat_invitations.add(chat_id)

    def accept_chat_join_requests(self, chat_id: int):
        if chat_id not in self.chat_invitations:
            raise ChatNotFoundException
        self.chat_invitations.remove(chat_id)
        chat = self.chat_platform.get_chat(chat_id)
        chat.add_member(self.id_)

    def reject_chat_join_requests(self, chat_id: int):
        if chat_id not in self.chat_invitations:
            raise ChatNotFoundException
        self.chat_invitations.remove(chat_id)

    def send_message(self, msg: str, chat_id: int):
        if chat_id not in self.chat_invitations:
            raise ChatNotFoundException
        chat = self.chat_platform.get(chat_id)
        chat.send_message(self.id_, msg)

    def message_notification(self, msg: str, user_id: int, chat_id: int):
        print(f"Message from {user_id} in chat {chat_id}: {msg}")