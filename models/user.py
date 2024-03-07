#!/usr/bin/python3

from models.base_model import BaseModel

class User(BaseModel):
    """
    A class represnting a user, inheriting from BaseModel.
    """

    def __init__(self, email="", password="", first_name="", last_name="", **kwargs):
        """
        Initializes a user with specific attributes.

        Args:
            email (str): The user's email address.
            password (str): The user's password.
            first_name (str): The user's first name.
            last_name (str): The user's last name.
            **kwargs: Additional keyword arguments for the base class.
        """
        super().__init__(**kwargs) #Call the base class constructor
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
