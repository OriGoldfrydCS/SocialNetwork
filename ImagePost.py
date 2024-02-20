from Post import Post
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os


# This subclass represents an ImagePost (which extents Post)
class ImagePost(Post):

    # A constructor for ImagePost (that uses his parent constructor)
    def __init__(self, user, image_name):
        # Check image_name is a non-empty string
        if not isinstance(image_name, str) or not image_name.strip():
            raise ValueError("Image name must be a non-empty string")

        # Check if image file exists
        # if not os.path.isfile(image_name):
        #     raise FileNotFoundError(f"Image file '{image_name}' not found")

        # File type validation (simple example)
        valid_extensions = ['.jpg', '.png', '.gif']
        _, file_extension = os.path.splitext(image_name)
        if file_extension.lower() not in valid_extensions:
            raise ValueError(f"Unsupported image format: {file_extension}")

        super().__init__(user)
        self.image_name = image_name

    # This method displays the image
    def display(self):
        try:
            image = mpimg.imread(self.image_name)
            plt.imshow(image)
            plt.axis('off')    # Turn off axis since it is a picture
            plt.show()
            print("Shows picture")
        except Exception as e:
            print(f"Failed to display image: {e}")

    # This method returns a message that a user posted an image
    def __str__(self):
        return f"{self.user.username} posted a picture\n"