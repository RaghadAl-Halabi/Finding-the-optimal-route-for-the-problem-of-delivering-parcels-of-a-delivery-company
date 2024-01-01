from State import State
from Position import Position
from GridInfo import GridInfo
from Truck import Truck

class Game:
  def __init__(self, Grid):
    self.gridInfo = GridInfo(Grid.length, Grid.width, Grid.startPosition)
    self.state = State (None, self.gridInfo, Truck(Grid.startPosition, []), Grid.buildings, Grid.receipts, Grid.delivers, Grid.startPosition)
  