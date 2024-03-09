#!/usr/bin/python3

from models.base_model import BaseModel

class Review(BaseModel):
    """
    A class representing a review, inheriting from BaseModel.
    """
    place_id = ""
    user_id = ""
    text = ""
