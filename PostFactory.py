from ImagePost import ImagePost
from SalePost import SalePost
from TextPost import TextPost


# This is a post factory for 3-types of posts: TextPost, ImagePost and SalePost
class PostFactory(type):
    @staticmethod
    def create_post(post_type, user, *args):
        if post_type == "Text":
            return TextPost(user, *args)
        elif post_type == "Image":
            return ImagePost(user, *args)
        elif post_type == "Sale":
            return SalePost(user, *args)
        else:
            raise ValueError("Invalid post type")
