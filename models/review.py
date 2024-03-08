#!/usr/bin/python3

from models.base_model import BaseModel

class Review(BaseModel):
    """
    A class representing a review, inheriting from BaseModel.
    """

    def __init__(self, place_id="", user_id="", text="", **kwargs):
        """
        Initializes a review with a place_id, user_id, and text.

        Args:
            place_id (str): The id of the place being reviewed.
            user_id (str): the id of the user writing the review.
            text (str): Text content of the review.
            **kwargs: Additional keyword arguments for the base class.
        """
        super().__init__(**kwargs)
        self.place_id = place_id
        self.user_id = user_id
        self.text = text

    def to_dict_review(self):
        review_dict = {
                'place_id' : self.palce_id,
                'user_id' : self.user_id,
                'text' : self.text
                }
        return review_dict
