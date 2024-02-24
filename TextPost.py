from Post import Post


# This subclass represents a TextPost (which extents Post)
class TextPost(Post):

    # A constructor
    def __init__(self, user, content):
        # Check if the content is empty
        if content is None:
            raise ValueError("Text post cannot be empty")

        # If valid input -> create an object
        super().__init__(user)
        self.content = content

    # This method returns a string of the user and the post shared
    def __str__(self):
        return f"{self.user.username} published a post:\n\"{self.content}\"\n"
