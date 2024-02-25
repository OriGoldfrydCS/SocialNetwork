from ImagePost import ImagePost
from SalePost import SalePost
from TextPost import TextPost


# This is a post factory for 3-types of posts: TextPost, ImagePost and SalePost
class PostFactory:

    @staticmethod
    def create_post(post_type, user, *args):
        if user is None:
            raise ValueError("Invalid user: user must be a User instance and cannot be None.")

        if post_type == "Text":
            # Ensure that args contains text content
            if len(args) != 1:
                raise ValueError("Text content cannot be empty for TextPost.")
            return TextPost(user, *args)

        elif post_type == "Image":
            # Ensure that args contains the image name
            if len(args) != 1:
                raise ValueError("ImagePost requires a valid image name.")
            return ImagePost(user, *args)

        elif post_type == "Sale":
            # Ensure that args contains all details regarding SalePost
            if len(args) != 3:
                raise ValueError("SalePost requires a title and a non-negative price.")
            return SalePost(user, *args)

        else:
            raise ValueError("Unknown post type. Available post types: Text, Image, Sale.")
