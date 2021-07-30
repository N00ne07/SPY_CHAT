from datetime import datetime

class Spy:

    def __init__(self, name, salutation, age):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.is_online = True
        self.chats = []
        self.current_status_message = None
        self.count = 0

class ChatMessage:
    def __init__(self, message, sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

spy = Spy('Noone', 'Mr.', 22)

friend_one = Spy('Reus', 'Mr.', 27)
friend_two = Spy('Ronaldo', 'Mr.', 21)
friend_three = Spy('Sarah', 'Ms.', 27)

friends = [friend_one, friend_two, friend_three]
