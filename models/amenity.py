#!/usr/bin/python3

from models.base_model import BaseModel

class Amenity(BaseModel):
    """
    A class representing an amenity, inheriting from BaseModel.
    """

    def __init__(self, name="", **kwargs):
        """
        Initializes an amenity with a name.

        Args:
            name (str): Name of the amenity.
            **kwargs: Additional keyword arguments for the base class.
        """
        super().__init__(**kwargs)
        self.name = name

    def to_dict_amenity(self):
        amenity_dict = {
                'name' : self.name
                }
        return amenity_dict
