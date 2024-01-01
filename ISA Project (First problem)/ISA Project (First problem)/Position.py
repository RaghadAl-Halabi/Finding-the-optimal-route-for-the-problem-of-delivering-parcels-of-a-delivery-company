class Position:
  def __init__(self, t):
         self.x = int(t[0])
         self.y = int(t[1])
  def __eq__(self, other):
        return self.x == int(other.x) and self.y == int(other.y)