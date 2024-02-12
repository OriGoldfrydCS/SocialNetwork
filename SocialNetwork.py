# This class represents a Network, which the functionalities below:
# 1) Can register new users (by choosing a username and password).
#    Note: (a) Each user has a unique username; (b) The password length is 4-8 characters.
# 2) The users can connect or disconnect from the network (after registration the user automatically connected).
# 3) A user can edit an activity only when he is connected (alerts can be received when the user is not connected).
# 4) It is forbidden to create more than one network while the program is running.
from User import User


class SocialNetwork:
    # Data members
    _name = None      # Class variable to store the network's name
    _instance = None  # Class variable to store the singleton instance of the network

    # A private constructor
    def __init__(self, name):
        self._name = name    # Set the social network's name
        self.users = {}      # Initialize a dictionary to store users

    # A constructor to ensure a singleton instance for Social Network
    def __new__(cls, name):
        # Establish a network only if no other instance already exists
        if cls._instance is None:
            cls._instance = super(SocialNetwork, cls).__new__(cls)
            cls._instance.__init__(name)
            print(f"The social network {name} was created!")  # Print message about establishment of social network
        return cls._instance

    # Methods
    # This method handles the registration process of a new user to the social network
    def sign_up(self, username, password):
        if username in self.users:         # Check if the username already exists
            print(f"Username '{username}' is already taken.")
            return None
        if not (4 <= len(password) <= 8):  # Check password validity
            print("Password must include 4 to 8 characters.")
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

    # Getter

    # This method return a string of the Social Network and the users registered
    def __str__(self):
        result = self._name + " social network:"
        for value in self.users.values():
            result += f"\n{value.__str__()}"
        return result
