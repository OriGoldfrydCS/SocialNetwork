# This class represents a Network, which the functionalities below:
# 1) Can register new users (by choosing a username and password).
#    Note: (a) Each user has a unique username; (b) The password length is 4-8 characters.
# 2) The users can connect or disconnect from the network (after registration the user automatically connected).
# 3) A user can edit an activity only when he is connected (alerts can be received when the user is not connected).
# 4) It is forbidden to create more than one network while the program is running.
from User import User


class SocialNetwork:
    # Data members
    _instance = None            # Class variable to store a singleton instance for network
    _is_first_instance = True   # Flag to check if the instance is being created for the first time

    # A constructor
    def __new__(cls, name):
        if not cls._instance:
            # Create a new instance
            cls._instance = super(SocialNetwork, cls).__new__(cls)
            # Initialize the instance
            cls.name = name  # Set the network name
            cls.users = {}                  # Initialize a dictionary to store users
            cls._is_first_instance = True   # Mark as initialized
            print(f"The social network {cls.name} was created!")  # Print creation message
        return cls._instance

    # Methods

    # This method handles the registration process of a new user to the social network
    def sign_up(self, username, password):
        if username in self.users:         # Check if the username already exists
            print(f"Username '{username}' is already taken.")
            return None
        if not (4 <= len(password) <= 8):  # Check password validity
            print("Password must include between 4 and 8 characters.")
            return None

        new_user = User(username, password)
        self.users[username] = new_user                 # Make sure to add the new_user to self.users
        self.users[username].set_connected(True)        # Correctly call log_in with username and password
        new_user.network = self                         # Set the network reference in the User object

        return new_user

    # This method handles the connect process of a user to the social network
    def log_in(self, username, password):
        user = self.users[username]
        if user:
            user.set_connected(True)
            print(f"{username} connected")

    # This method handles the connect process of a user to the social network
    def log_out(self, username):
        user = self.users[username]
        if user:
            user.set_connected(False)
            print(f"{username} disconnected")

    # This method return the Social Network and the users registered
    def __str__(self):
        result = self.name + " social network:\n"
        for value in self.users.values():
            result += f"{value.__str__()}\n"
        return result
