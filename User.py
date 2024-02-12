# This class represents a User object, and enable them to use the Network
from PostFactory import PostFactory


class User:

    # A constructor for new user
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.is_connected = False   # A boolean flag -> connected (true) or disconnected (false)
        self.followers = []         # A list that stores other users that follow this user
        self.following = []         # A list that stores users this user is following
        self.posts = []             # A list that stores user's posts
        self.notifications = []     # A list that stores string notifications for the user

    # This method enables a user to follow other user
    def follow(self, other_user):
        if self.is_connected:           # A user can follow other user only when he is logged in
            if self == other_user:      # A user cannot follow himself
                return
            if other_user.username not in self.following:  # A user can follow a user who is not in his following list
                self.following.append(other_user)
                other_user.followers.append(self)
                print(f"{self.username} started following {other_user.username}")  # Print follow  message

    # This method enables a user to unfollow other user
    def unfollow(self, other_user):
        if self.is_connected:           # A user can unfollow other user only when he is logged in
            if self == other_user:      # A user cannot unfollow himself
                return
            if other_user in self.following:       # A user can unfollow a user who is already in his following list
                self.following.remove(other_user)  # Remove other_user from this user's following list
                other_user.followers.remove(self)  # Remove this user from other_user's followers list
                print(f"{self.username} unfollowed {other_user.username}")
            else:
                print(f"{self.username} is not following {other_user.username}")
        else:                           # The user is not connected -> return nothing
            return

    # This method add a notification to the user's list
    def get_notification(self, msg):
        self.notifications.append(msg)

    # This method enables a user to publish a post of a specified type
    def publish_post(self, post_type, *args):
        if self.is_connected:           # A user can unfollow other user only when he is logged in
            post = PostFactory.create_post(post_type, self, *args)  # Create the specific post with PostFactory
            self.posts.append(post)                                       # Append the post to the user post's list
            for user in self.followers:
                user.get_notification(f"{self.username} has a new post")  # Send notifications to all user's followers
            print(post)                                                   # That implements observer design pattern
            return post
        else:                           # The user is not connected -> return nothing
            return

    # This method prints the user list notifications
    def print_notifications(self):
        print(f"{self.username}'s notifications:")
        for notification in self.notifications:
            print(notification)

    # This method changes the user's connection mode
    def set_connected(self, mode):
        self.is_connected = mode

    # This method compares two users and returns true in case of identical objects; otherwise, false
    def __eq__(self, other):
        if isinstance(other, User):
            return self.username == other.username
        return False

    # This method returns the user details
    def __str__(self):
        return "User name: " + self.username + ", Number of posts: " + str(len(self.posts)) \
            + ", Number of followers: " + str(len(self.followers))