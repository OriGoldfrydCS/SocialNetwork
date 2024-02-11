from abc import ABC, abstractmethod


# This class represents an abstract Post object
class Post(ABC):

    # A constructor for generic post
    def __init__(self, user):
        self.user = user    # The user who created the post
        self.likes = 0      # Number of likes the post has received
        self.comments = []  # List of comments on the post

    # A method that increments the number of likes for a post
    def like(self, the_user):
        if self.user == the_user:
            return
        self.likes += 1
        self.user.get_notification(f"{the_user.username} liked your post");
        print(f"notification to {self.user.username}: {the_user.username} liked your post")

    # A method that adds a comment to the post
    def comment(self, the_user, comment):
        if self.user == the_user:
            return
        self.user.get_notification(f"{the_user.username} commented on your post");
        print(f"notification to {self.user.username}: {the_user.username} commented on your post: {comment}")

    # A method that counts the like on a post
    def add_like(self):
        self.likes += 1

    # Enforces subclasses to implement toString method, since a Post is not an object in his abstract form
    @abstractmethod
    def __str__(self):
        pass
