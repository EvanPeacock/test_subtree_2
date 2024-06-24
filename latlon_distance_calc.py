import math

# Function to calculate new lat and lon given a starting lat, lon, heading, and distance
# Initially created to place visual aids correctly in the sim in relation to the center of the helipad

def calculate_new_lat_lon(lat, lon, heading, distance):
    R = 20903520  # Radius of the Earth in feet
    brng = math.radians(heading)  # heading in degrees converted to radians

    lat1 = math.radians(lat)  # Current lat point converted to radians
    lon1 = math.radians(lon)  # Current long point converted to radians

    lat2 = math.asin(math.sin(lat1) * math.cos(distance / R) +
                     math.cos(lat1) * math.sin(distance / R) * math.cos(brng))

    lon2 = lon1 + math.atan2(math.sin(brng) * math.sin(distance / R) * math.cos(lat1),
                             math.cos(distance / R) - math.sin(lat1) * math.sin(lat2))

    lat2 = math.degrees(lat2)
    lon2 = math.degrees(lon2)

    return lat2, lon2

print(calculate_new_lat_lon(49.211806766, -122.701606501, 274.98, 50))
print(calculate_new_lat_lon(49.211806766, -122.701606501, (274.98 + 45), 50))
print(calculate_new_lat_lon(49.211806766, -122.701606501, (274.98 + 90), 50))
