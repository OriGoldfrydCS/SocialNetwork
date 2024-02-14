from abc import ABC, abstractmethod


# Sender interface
class Sender(ABC):

    # A constructor which initiates the followers list, means the user's subscribers
    def __init__(self):
        self._followers = []

    # "Register" a follower to the followers list
    def register(self, follower):
        self._followers.append(follower)

    # "Unregister" a follower from the followers list
    def unregister(self, follower):
        self._followers.remove(follower)

    # Notify all followers (subscribers) about an event, means publishing of a post
    def notify(self, event):
        for follower in self._followers:
            follower.update(event)


# Observer interface
class Member(ABC):

    @abstractmethod
    def update(self, event):
        pass
