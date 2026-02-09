from geopy.distance import geodesic
from typing import List
from .models import Address


def get_addresses_within_distance(
    addresses: List[Address],
    latitude: float,
    longitude: float,
    max_distance_km: float
):
    nearby_addresses = []

    user_location = (latitude, longitude)

    for address in addresses:
        address_location = (address.latitude, address.longitude)
        distance = geodesic(user_location, address_location).kilometers

        if distance <= max_distance_km:
            nearby_addresses.append(address)

    return nearby_addresses
