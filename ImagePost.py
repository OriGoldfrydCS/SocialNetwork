from Post import Post
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


# This subclass represents an ImagePost (which extents Post)
class ImagePost(Post):

    # A constructor for ImagePost (that uses his parent constructor)
    def __init__(self, user, image_name):
        super().__init__(user)
        self.image_name = image_name

    # This method displays the image
    def display(self):
        image = mpimg.imread(self.image_name)
        plt.imshow(image)
        plt.axis('off')     # Turn off axis since it is a picture
        plt.show()
        print("Shows picture")

    # This method returns a message that a user posted an image
    def __str__(self):
        return f"{self.user.username} posted a picture\n"
