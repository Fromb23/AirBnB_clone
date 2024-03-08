#!/usr/bin/python3

from models.base_model import BaseModel

class State(BaseModel):
    """
    A class representing a state, inheriting from BaseModel.
    """

    def __init__(self, name="", **kwargs):
        """
        Initializes a state with a name.

        Args:
            name (str): The name of the state
            **kwargs: Additional keyword arguments for the base class.
        """
        super().__init__(**kwargs)
        self.name = name
