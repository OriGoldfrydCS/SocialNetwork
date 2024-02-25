from abc import ABC, abstractmethod


# This class represents an abstract Post object
class Post(ABC):

    # A constructor for generic post
    def __init__(self, user):
        # Check user validation
        if user is None:
            raise ValueError("Invalid user")

        # If valid input -> create an object
        self.user = user            # The user who created the post
        self.likes = 0              # Number of likes a post has received
        self.likes_list = []        # List that sores the users that like the post
        self.comments = []          # List of comments on the post

    # A method that adds a like to a post
    # NOTE: a user can like his own post but will not receive a notification on his act
    def like(self, the_user):
        # a user can like a post -    (1) if he/she is registered to the network; and
        #                             (2) if he/she is connected to the network; and
        #                             (3) twice or more
        if the_user.username in the_user.network.users and the_user.is_connected \
                and the_user.username not in self.likes_list and self.user.username in the_user.network.users:
            self.add_like()  # increment the likes on a post
            self.likes_list.append(the_user.username)  # Track the users that like the post to prevent double-likes
            if self.user is not the_user:  # force that the user will not receive a notification on his own act
                self.user.update(f"{the_user.username} liked your post")
                print(f"notification to {self.user.username}: {the_user.username} liked your post")
            else:
                pass  # The user likes his own post -> return nothing with no notification msg
        # Exceptions
        else:
            if the_user.username in self.likes_list:  # A user tries to like the post twice or more
                raise ValueError("The user cannot like this post more than once")
            if the_user.username not in the_user.network.users:
                raise ValueError("The user is not registered to the network")
            if not the_user.is_connected:
                raise ValueError("The user is disconnected")
            if self.user.username not in the_user.network.users:
                raise ValueError("Post does not exist")
        return

    # A method that adds a comment to a post
    def comment(self, the_user, comment):
        # a user can comment on a post -    (1) if he/she is registered to the network; and
        #                                   (2) if he/she is connected to the networkl
        if the_user.username in the_user.network.users and the_user.is_connected and self.user.username in the_user.network.users:
            self.add_comment(comment)
            if self.user is not the_user:  # force that a user will not receive a notification on his own act
                self.user.update(f"{the_user.username} commented on your post");
                print(f"notification to {self.user.username}: {the_user.username} commented on your post: {comment}")
            else:
                pass  # The user comments on his own post -> return nothing with no notification msg
        # Exceptions
        else:
            if the_user.username in self.likes_list:  # A user tries to comment on a post twice or more
                raise ValueError("The user cannot comment on that post")
            if the_user.username not in the_user.network.users:
                raise ValueError("The user is not registered to the network")
            if not the_user.is_connected:
                raise ValueError("The user is disconnected")
            if self.user.username not in the_user.network.users:
                raise ValueError("Post does not exist")
        return

    # A method that increments the number of likes for a post
    def add_like(self):
        self.likes += 1

    # A method that append a comment to the comments list on a post
    def add_comment(self, comment):
        self.comments.append(comment)

    # Enforces subclasses to implement toString method, since a Post is not an object in his abstract form
    @abstractmethod
    def __str__(self):
        pass
