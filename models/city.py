#!/usr/bin/python3


from models.base_model import BaseModel

class City(BaseModel):
    """
    A class representing a city, inheriting from BaseModel.
    """

    def __init__(self, state_id="", name="", **kwargs):
        """
        Initializes a city with state_id and name.

        Args:
            state_id (str): Id of the state which the city belongs.
            name (str): Name of the city.
            **kwargs: Additional keyword argumenents for the base class.
        """
        super().__init__(**kwargs)
        self.state_id = state_id
        self.name = name
