from abc import ABC, abstractmethod


# Sender interface
class Sender(ABC):

    # A constructor which initiates the followers list, means the user's subscribers
    def __init__(self):
        self._followers = []

    # "Register" a follower to the followers list
    def register(self, follower):
        if not isinstance(follower, Member) and self in self._followers:
            raise ValueError("Follower must implement Member interface")
        if self in self._followers:
            raise ValueError("Follower is already int the followers list")
        self._followers.append(follower)

    # "Unregister" a follower from the followers list
    def unregister(self, follower):
        if follower not in self._followers:
            raise ValueError("Follower not found in followers list")
        self._followers.remove(follower)

    # Notify all followers (subscribers) about an event, means publishing of a post
    def notify(self, event):
        if event is None:
            raise ValueError("Event cannot be None")
        for follower in self._followers:
            if follower is not None:        # Additional check for follower validity
                follower.update(event)


# Observer interface
class Member(ABC):

    @abstractmethod
    def update(self, event):
        pass
