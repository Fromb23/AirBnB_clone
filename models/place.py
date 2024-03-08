#!/usr/bin/python3

from models.base_model import BaseModel

class Place(BaseModel):
    """
    A class representing a place, inheriting from BaseModel.
    """

    def __init__(self, city_id="", user_id="", name="", description="",
            number_rooms=0, number_bathrooms=0, max_guest=0, price_by_night=0,
            latitude=0.0, longitude=0.0, amenity_ids=None, **kwargs):

        """
        Initializes a place with various attributes.

        Args:
            city_id (str): Id of the city where the place is located.
            user_id (str): Id of the user who owns the place
            name (str): Name of the place.
            description (str): Description of the place.
            number_rooms (int): Number of rooms in the place.
            number_bathrooms (int): Number of bathrooms in the place.
            max_guest (int): Max number of guests the place can accomodate.
            price_by_night (int): Price per night for the place.
            latitude (float): Latitude coordinate of the place.
            longitude (float): Longitude coordinate of the place.
            amenity_ids (list): List of amenity ids associated with the place.
            **kwargs: Additional keywor arguments for the base class.
        """
        super().__init__(**kwargs)
        self.city_id = city_id
        self.user_id = user_id
        self.name = name
        self.description = description
        self.number_rooms = number_rooms
        self.number_bathrooms = number_bathrooms
        self.max_guest = max_guest
        self.price_by_night = price_by_night
        self.latitude = latitude
        self.longitude = longitude
        self.amenity_id = amenity_ids or []

        def to_dict_place(self):
            place_dict = {
                    'city_id' : self.city_id,
                    'user_id' : self.user_id,
                    'name' : self.name,
                    'description' : self.description,
                    'number_rooms' : self.number_rooms,
                    'number_bathrooms' : self.number_bathrooms,
                    'max_guest' : self.max_guest,
                    'price_by_night' : self.price_by_night,
                    'latitude' : self.latitude,
                    'longitude' : self.longitude,
                    'amenity_id' : self.amenity_id
                    }
            return place_id
