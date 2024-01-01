from Game import Game
from A_star import A_star
from Grid import Grid
import termcolor

# Initialize the Grid
Grid = Grid()
print('Choose the Grid')
gridNumber = int(input())
if(gridNumber == 0):
    Grid.Grid0()
if(gridNumber == 1):
    Grid.Grid1()
if(gridNumber == 2):
    Grid.Grid2()
if(gridNumber == 3):
    Grid.Grid3()


    

# Run the Game
g = Game(Grid)
if not g.state.checkInput():
  print("Invalid Input!")
else:
   print('Choose Game Configuration')
   print('0. UCS')
   print('1. A* heuristic 1')
   print('2. A* heuristic 2')
   print('3. A* heuristic 3')
   print('4. A* all heuristics')
   print('press any other key to close')

   modeNumber = int(input())
   if(modeNumber == 0):
      termcolor.cprint('Algorithm : UCS', 'cyan')
      g.state.ucs()
   elif(modeNumber == 1 or modeNumber == 2 or modeNumber == 3 or modeNumber == 4):
       if(modeNumber == 4):
          termcolor.cprint('Algorithm : A* All Heuristics ', 'cyan')
       else:
          termcolor.cprint('Algorithm : A* Heuristic ' + str(modeNumber), 'cyan')
       A = A_star(g.state)
       A.run(modeNumber)