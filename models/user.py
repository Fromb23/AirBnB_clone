#!/usr/bin/python3

from models.base_model import BaseModel

class User(BaseModel):
    """
    A class represnting a user, inheriting from BaseModel.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
