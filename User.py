from NotifyManager import Sender, Member
from PostFactory import PostFactory


# This class represents a user object
class User(Sender, Member):

    # A constructor for new user
    def __init__(self, username, password, network=None):
        super().__init__()          # Initialize the Sender part of User (means the follower list, means subscribers)
        self.username = username
        self.password = password
        self.network = network      # Store the SocialNetwork reference
        self.is_connected = False   # A boolean flag -> connected (true) or disconnected (false)
        self.following = []         # A list that stores users this user is following (means subscriptions)
        self.posts = []             # A list that stores user's posts
        self.notifications = []     # A list that stores string notifications for the user

    # This method enables a user to follow other user
    def follow(self, other_user):
        # a user can follow other_user - (1) if both of them registered to the network; and
        #                                (2) only when the user is logged in; and
        #                                (3) A user cannot follow himself; and
        #                                (4) A user can follow a user other who is not in his following list
        if self.username in self.network.users and other_user.username in self.network.users \
                and self.is_connected and self != other_user and other_user not in self.following:
            self.following.append(other_user)   # add other_user from this user's following list
            other_user.register(self)           # Subscribe this user to get notifications from the other user
            print(f"{self.username} started following {other_user.username}")
        else:
            raise ValueError("The user cannot follow that other user")

    # This method enables a user to unfollow other user
    def unfollow(self, other_user):
        # a user can unfollow other_user - (1) if both of them registered to the network; and
        #                                  (2) only when the user is logged in; and
        #                                  (3) A user cannot unfollow himself; and
        #                                  (4) A user can unfollow a user other who is not in his following list
        if self.username in self.network.users and other_user.username in self.network.users \
                and self.is_connected and self != other_user and other_user in self.following:
            self.following.remove(other_user)   # Remove other_user from this user's following list
            other_user.unregister(self)         # Subscribe this user to get notifications from the other user
            print(f"{self.username} unfollowed {other_user.username}")
        else:
            raise ValueError("The user cannot unfollow that other user")

    # This method add a notification to the user's list
    def update(self, event):
        self.notifications.append(event)

    # This method enables a user to publish a post of a specified type
    def publish_post(self, post_type, *args):
        # A user can publish a post only when he is registered and logged in
        if self.is_connected and self.username in self.network.users:
            post = PostFactory.create_post(post_type, self, *args)  # Create the specific post with PostFactory
            self.posts.append(post)                           # Append the post to the user post's list
            self.notify(f"{self.username} has a new post")    # Send notifications to all user's followers (subscribers)
            print(post)
            return post
        else:                           # The user is not connected -> return nothing
            raise ValueError("The user cannot publish that post")

    # This method prints the user list notifications
    def print_notifications(self):
        if self.notifications is not None:
            print(f"{self.username}'s notifications:")
            for notification in self.notifications:
                print(notification)

    # This method changes the user's to connect
    def set_connected(self):
        self.is_connected = True

    # This method changes the user's to disconnect
    def set_disconnected(self):
        self.is_connected = False

    # This method compares two users and returns true in case of identical objects; otherwise, false
    def __eq__(self, other):
        if isinstance(other, User):
            return self.username == other.username
        return False

    # This method returns the user details
    def __str__(self):
        return "User name: " + self.username + ", Number of posts: " + str(len(self.posts)) \
            + ", Number of followers: " + str(len(self._followers))