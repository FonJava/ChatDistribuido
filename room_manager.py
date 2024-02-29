# room_manager.py
from flask_socketio import emit

class User:
    def __init__(self, username):
        self.username = username

class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, username):
        self.users = [user for user in self.users if user.username != username]

class RoomManager:
    def __init__(self):
        self.rooms = {}

    def create_room(self, room_name):
        if room_name not in self.rooms:
            self.rooms[room_name] = Room(room_name)

    def get_all_rooms(self):
        return list(self.rooms.keys())

    def get_room(self, room_name):
        return self.rooms.get(room_name)

    def remove_room(self, room_name):
        if room_name in self.rooms:
            del self.rooms[room_name]

class Room:
    def __init__(self, room_name):
        self.room_name = room_name
        self.users = set()

    def join(self, username):
        self.users.add(username)

    def leave(self, username):
        self.users.remove(username)

    def send_message(self, username, message):
        for user in self.users:
            emit('message', f'{username}: {message}', room=user)
