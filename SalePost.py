import string
from Post import Post


# This subclass represents a SalePost (which extents Post)
class SalePost(Post):

    # A constructor
    def __init__(self, user, content, price, location, availability=True):
        # Check if price is less than zero or the content/location is empty
        if price < 0:
            raise ValueError("Price cannot be negative")
        if content is None:
            raise ValueError("Sale post cannot be empty with sale's details")
        if location is None:
            raise ValueError("Sale post cannot be empty with location")

        # If valid input -> create an object
        super().__init__(user)
        self.content = content              # A variable that represents item for sale
        self.price = price                  # A variable that represents the item's price
        self.location = location            # A variable that represents the item's location
        self.availability = availability    # A variable that represents availability of an item

    # This method calculates the discount given
    def discount(self, percentage, password):
        if not 0 <= percentage <= 100:
            raise ValueError("Discount percentage must by between 0 to 100")

        if self.user.password == password:
            self.price *= (1 - percentage / 100)
            print(f"Discount on {self.user.username} product! the new price is: {str(self.price)}")

    # This method handles a case where an item already sold
    def sold(self, password):
        if self.user.password != password:
            raise ValueError("Incorrect password")
        self.availability = False
        print(f"{self.user.username}'s product is sold")

    # This method changes the item's mode from available to unavailable
    def mark_as_sold(self):
        self.availability = False

    # This method returns a sting the represents the item status ("for sale" or "sold")
    def __str__(self):
        if self.availability is True:
            return f"{self.user.username} posted a product for sale:\n" \
                   f"For sale! {self.content}, price: {self.price}, pickup from: {self.location}\n"
        elif self.availability is False:
            return f"{self.user.username} posted a product for sale:\n" \
                   f"Sold! {self.content}, price: {self.price}, pickup from: {self.location}\n"
        else:
            raise ValueError("Something went wrong...")
