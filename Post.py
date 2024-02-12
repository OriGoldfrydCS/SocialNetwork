from abc import ABC, abstractmethod


# This class represents an abstract Post object
class Post(ABC):

    # A constructor for generic post
    def __init__(self, user):
        self.user = user    # The user who created the post
        self.likes = 0      # Number of likes the post has received
        self.comments = []  # List of comments on the post

    # A method that adds a like to a post (a user can like his own post but will not receive a notification on his act)
    def like(self, the_user):
        self.add_like()
        if self.user is not the_user:   # force that a user will not receive a notification on his own act
            self.user.get_notification(f"{the_user.username} liked your post")
            print(f"notification to {self.user.username}: {the_user.username} liked your post")
        else:
            return                       # The user likes his own post -> return nothing with no notification msg

    # A method that adds a comment to a post
    def comment(self, the_user, comment):
        self.add_comment(comment)
        if self.user is not the_user:   # force that a user will not receive a notification on his own act
            self.user.get_notification(f"{the_user.username} commented on your post");
            print(f"notification to {self.user.username}: {the_user.username} commented on your post: {comment}")
        else:
            return                      # The user comments on his own post -> return nothing with no notification msg

    # A method that increments the number of likes for a post
    def add_like(self):
        self.likes += 1

    # A method that append a comment to the comments list on a post
    def add_comment(self, comment):
        self.comments.append(comment)

    # Enforces subclasses to implement toString method, since a Post is not an object in his abstract form
    @abstractmethod
    def __str__(self):
        return


