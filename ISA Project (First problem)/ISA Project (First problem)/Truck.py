  # import Position
class Truck:
    def __init__(self, position, parcels):
      # position: truck current position (Position)
      # parcels: list of parcelIDs in the truck
         self.position = position
         self.parcels = parcels
    def __eq__(self, other):
       return self.position == other.position and self.parcels == other.parcels