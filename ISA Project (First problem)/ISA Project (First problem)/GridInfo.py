# import Position
class GridInfo:

#(n-1,0)   (n-1, m-1)
# ___________
#|           |
#|           |
#|           |
#|___________|
#(0,0)    (0,m-1)
  def __init__(self, n, m, goalPosition):
         # cells number in one column
         self.n = int(n)
         # cells number in one row
         self.m = int(m)
         # Truck start position
         self.goalPosition = goalPosition
  def __eq__(self, other):
       return self.n == int(other.n) and self.m == int(other.m) and self.goalPosition == other.goalPosition