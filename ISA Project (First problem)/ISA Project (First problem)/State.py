from Truck import Truck
from Position import Position
from GridInfo import GridInfo
import termcolor
import time

class State:
    def __init__(self, parent, gridInfo, truck, buildings, receipts, delivers, startPosition):
      # parent: The previous state for the current one (State)
      # gridInfo: grid information (GridInfo)
      # truck: truck attributes (Truck)
      # buildings: list of buildings positions (list(Position))
      # receipts: list of tuples (receipt position, parcelID in this position) (list((Position, parcelID)))
      # delivers: list of tuples (delivery position, parcelID in this position) (list((Position, parcelID)))
         self.parent = parent
         self.gridInfo = gridInfo 
         self.truck = truck
         self.buildings = buildings
         self.receipts = receipts
         self.delivers = delivers
         self.start = startPosition
         

    def __eq__(self, other):
        if other!=None and self!=None:
          return self.gridInfo == other.gridInfo and self.truck == other.truck and self.buildings == other.buildings and self.receipts == other.receipts and self.delivers == other.delivers
        return False

 
    def checkReceiptsAndDelivers(self):
      import copy
      tempReceipts = copy.deepcopy(self.receipts)
      tempDelivers = copy.deepcopy(self.delivers)

      while len(tempReceipts):
          found = [(tempReceipts[0], td) for td in tempDelivers if td[1] == tempReceipts[0][1] ]
          if len(found) != 1:
            return False
          else:
            tempReceipts.remove(found[0][0])
            tempDelivers.remove(found[0][1])  

      if len(tempReceipts) or len(tempDelivers):
        return False
      return True  
   
   
   
    def checkInput(self):
      return self.inLimits([self.gridInfo.goalPosition], self.buildings, list(zip(*self.receipts))[0], list(zip(*self.delivers))[0]) \
       and self.checkReceiptsAndDelivers()     
        
    def inLimits(self, *args):
      for positions in args:
          for position in positions:
              if (position.x < 0 or position.x > (self.gridInfo.n)-1) \
            or \
              (position.y < 0 or position.y > (self.gridInfo.m)-1): 
                  return False
              # print(position.y, (self.gridInfo.m)-1, position.y > (self.gridInfo.m)-1)    
      return True     
 
    def canMoveTruckTo(self, position):
        return self.inLimits([position]) and not position in self.buildings

    def canReceive(self, position):
        return len([True for receipt in self.receipts if receipt[0] == position])
       
    def getReceivedParcelID(self, position):
      return [receipt[1] for receipt in self.receipts if receipt[0] == position] [0]
    
    # this function is used to make sure that we can deliver this specific parcel from this position
    def canDeliverPP(self, parcelID, position):
        return (position, parcelID) in self.delivers and parcelID in self.truck.parcels

    # this function is used to make sure that we can deliver a parcel from this position
    def canDeliverP(self, position):
        return len([True for delivery in self.delivers if delivery[0] == position])
    
    # this function is used to get the parcelID if the previous function was true
    def getDeliveredParcelID(self, position):
        return [delivery[1] for delivery in self.delivers if delivery[0] == position] [0]  

    def endState(self):
      # It is not necessary to check the emptiness of self.receipts because the emptiness of self.delivers emplies this
        return self.truck.position ==  self.gridInfo.goalPosition and len(self.delivers) == 0

    def receive(self, parcelID):
        self.receipts.remove((self.truck.position, parcelID))
        self.truck.parcels.append(parcelID)

    def deliver(self, parcelID):
        self.delivers.remove((self.truck.position, parcelID))
        self.truck.parcels.remove(parcelID)

    def moveTruckTo(self, to):
        self.truck.position = to
          
    def generateState(self, action, info):
        import copy
      # A new state could be generated due to a move or a receive or a deliver
        myState = copy.deepcopy(self)
        myState.parent = copy.deepcopy(self)
        if action == 0:
          # It is a move, and info would be a position
          myState.moveTruckTo(info)
        elif action == 1:
          # It is a receive, and info would be a parcelID
          myState.receive(info)
        elif action == 2:
          # It is a deliver, and info would be a parcelID
          myState.deliver(info)    
        return myState

    def generatePossibleNextIntStates(self):
        intStates=[]

         # We have four different directions to move to, those are: up, down, right, left in order
        directions = [None]*4       
        
        directions[0] = Position((self.truck.position.x, self.truck.position.y+1))
        directions[1] = Position((self.truck.position.x, self.truck.position.y-1))
        directions[2] = Position((self.truck.position.x+1, self.truck.position.y))
        directions[3] = Position((self.truck.position.x-1, self.truck.position.y))

        for i, position in enumerate(directions):
            if self.canMoveTruckTo(position):
              # 0 is just to say that this is a move state
               intStates.append((0, position))
      
       # Check whether can we receive || deliver in truck position      
        if self.canReceive(self.truck.position):
          # 1 is just to say that this is a receive state
               intStates.append((1, self.getReceivedParcelID(self.truck.position)))
        for j, parcelID in enumerate(self.truck.parcels):
             if self.canDeliverPP(parcelID, self.truck.position):
                # 2 is just to say that this is a deliver state
                intStates.append((2, parcelID))
                           
                                          
        # self.currentState.show()
        # print(intStates)
        return intStates

    def show(self,num):
         num +=1
         print("state: "+str(num))
         for i in reversed(range(self.gridInfo.n,)):
             for j in range(self.gridInfo.m):
                 if Position((i, j)) in self.buildings:
                    termcolor.cprint("#", 'red',attrs = ['blink'], end=' \t')
                 elif self.truck.position == Position((i, j)):
                     termcolor.cprint("T", 'yellow', end=' ')
                     if self.canReceive(Position((i, j))):
                       termcolor.cprint("P"+str(self.getReceivedParcelID(Position((i, j)))),'cyan',end ='  ')
                     if self.canDeliverP(Position((i,j))):
                        termcolor.cprint("D"+str(self.getDeliveredParcelID(Position((i, j)))), 'magenta' ,end = '  ')
                     print("\t", end='')  
                 elif self.canReceive(Position((i, j))):
                       termcolor.cprint("P"+str(self.getReceivedParcelID(Position((i, j)))),'cyan', end ='  ')
                       if self.canDeliverP(Position((i,j))):
                        termcolor.cprint("D"+str(self.getDeliveredParcelID(Position((i, j)))), 'magenta', end = '  ')
                       print("\t", end='') 
                 elif self.canDeliverP(Position((i,j))):
                         termcolor.cprint("D"+str(self.getDeliveredParcelID(Position((i, j)))), 'magenta', end = ' \t')           
                 else:
                    termcolor.cprint(".",'white', end = '\t')
                 
             print("\n")
         print("\n")

    def ucs(self):
      t = time.time()
      import copy
      visited = []
      pqueue = []
      pqueue.append((0, copy.deepcopy(self)))
      statesCounter = 0

      while pqueue:
        cost, node = pqueue.pop(0)
        statesCounter += 1

        if node in visited:
          continue

        visited.append(node)    

        if node.endState():
          solution = []
          p1 = 0
          
          termcolor.cprint('Execution Time: ' + str(time.time() - t), 'red')
          termcolor.cprint("Visited : " + str(len(visited)), 'green')
          termcolor.cprint("Processed States Number: " + str(statesCounter), 'blue')
          termcolor.cprint("Final Total Cost: " + str(cost), 'yellow')

          while node != None:
            solution.append(node)
            node = copy.deepcopy(node.parent)
          termcolor.cprint('Moves Number: ' + str(len(solution) - 1 - (len(self.delivers) * 2)), 'magenta')      
          # while solution:
          #   s1 = solution.pop()
          #   time.sleep(0.8)
          #   s1.show(p1)
          #   p1+=1
          return solution

        for intState in node.generatePossibleNextIntStates():          
            neighbour = node.generateState(intState[0], intState[1])
            if not neighbour in visited:
                  if intState[0] == 0:
                    total_cost = cost + 1 + len(neighbour.truck.parcels)
                  elif intState[0] == 1:
                      total_cost = cost + 1
                  elif intState[0] == 2:
                      total_cost = cost - 1

                  add = False 
                  found = False   
                  for v in pqueue:
                    if v[1] == neighbour:
                      found = True
                      if v[0] > total_cost: 
                        add = True
                        pqueue.remove(v)

                  if add or not found:      
                    pqueue.append((total_cost, copy.deepcopy(neighbour)))
                    
        pqueue = sorted(pqueue, key = lambda x : x[0])
