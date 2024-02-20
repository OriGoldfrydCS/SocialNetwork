from ImagePost import ImagePost
from SalePost import SalePost
from SocialNetwork import User
from TextPost import TextPost


# This is a post factory for 3-types of posts: TextPost, ImagePost and SalePost
class PostFactory:

    @staticmethod
    def create_post(post_type, user, *args):
        if user is None or not isinstance(user, User):
            raise ValueError("Invalid user: user must be a User instance and cannot be None.")

        if post_type == "Text":
            # For TextPost, ensure there is text content in args
            if len(args) < 1 or not isinstance(args[0], str) or not args[0].strip():
                raise ValueError("Text content cannot be empty for TextPost.")
            return TextPost(user, *args)
        elif post_type == "Image":
            if len(args) < 1 or not isinstance(args[0], str) or not args[0].strip():
                raise ValueError("ImagePost requires a valid image name.")
            return ImagePost(user, *args)
        elif post_type == "Sale":
            if len(args) < 2 or not isinstance(args[0], str) or not args[0].strip() \
                    or not isinstance(args[1], (int, float)) or args[1] < 0:
                raise ValueError("SalePost requires a title and a non-negative price.")
            return SalePost(user, *args)
        else:
            raise ValueError("Unknown post type. Available types only: Text, Image, Sale.")
