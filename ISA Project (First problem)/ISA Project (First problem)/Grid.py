from Position import Position
from GridInfo import GridInfo

class Grid:
    def __init__(self) -> None:
        pass
    def Grid0(self):
        print("Enter truck starting position as (x,y): ")
        startPosition = Position(tuple(input().replace(') ','').replace(')','').replace('(','').split(',')))
        self.gridInfo = GridInfo(int(input("Enter n: ")), int(input("Enter m: ")), startPosition)
    
        self.buildings = []

        print("Enter buildings positions as (x1,y1), (x2,y2), ...: ")
        for building in input().split('), ('):
            building = building.replace(') ','').replace(')','').replace('(','')
            #tup looks like `a,a` or `b,b`
        self.buildings.append(Position(tuple(building.split(','))))

        receipts = []
        print("Enter receipts positions and parcelsIDs as ((x1,y1), parcelID1), ((x2,y2), parcelID2), ...: ")
        for receipt in input().split('), ('):    
            receipt = receipt.replace(') ','').replace(')','').replace('(','')
            receipt = list(receipt.split(', '))
            receipt[0].replace(') ','').replace(')','').replace('(','')
            receipt[0] = Position(tuple(receipt[0].split(',')))
            receipt[1] = int(receipt[1])

            #tup looks like `a,a` or `b,b`
        receipts.append(tuple((receipt[0], receipt[1])))

        delivers = []
        print("Enter delivers positions and parcelsIDs as ((x1,y1), parcelID1), ((x2,y2), parcelID2), ...: ")
        for deliver in input().split('), ('):
            deliver = deliver.replace(') ','').replace(')','').replace('(','')      
            deliver = list(deliver.split(', '))
            deliver[0].replace(') ','').replace(')','').replace('(','')
            deliver[0] = Position(tuple(deliver[0].split(',')))
            deliver[1] = int(deliver[1])

            #tup looks like `a,a` or `b,b`
        delivers.append(tuple((deliver[0], deliver[1])))
           
    def Grid1(self):
        # Start point
        self.startPosition = Position((3,6))
        # Dimentios of the Grid
        self.length = 4
        self.width = 7
        # Buildings 
        self.buildings = []
        self.buildings.append(Position((0,3)))
        self.buildings.append(Position((1,3)))
        self.buildings.append(Position((2,2)))
        self.buildings.append(Position((2,3)))
        self.buildings.append(Position((2,5)))
        self.buildings.append(Position((3,5)))
        # Receipts 
        self.receipts = []
        self.receipts.append((Position((2,1)), 0))
        # Delivers
        self.delivers = []
        self.delivers.append((Position((1,0)), 0))

    def Grid2(self):
        # Start point
        self.startPosition = Position((3,6))
        # Dimentios of the Grid
        self.length = 4
        self.width = 7
        # Buildings 
        self.buildings = []
        self.buildings.append(Position((0,5)))
        self.buildings.append(Position((1,3)))
        self.buildings.append(Position((2,2)))
        self.buildings.append(Position((2,3)))
        self.buildings.append(Position((2,5)))
        self.buildings.append(Position((3,5)))
        # Receipts 
        self.receipts = []
        self.receipts.append((Position((1,2)), 0))
        # Delivers
        self.delivers = []
        self.delivers.append((Position((0,6)), 0))

    def Grid3(self):
        # Start point
        self.startPosition = Position((3,3))
        # Dimentios of the Grid
        self.length = 4
        self.width = 7
        # Buildings 
        self.buildings = []
        self.buildings.append(Position((1,2)))
        self.buildings.append(Position((1,4)))
        self.buildings.append(Position((2,2)))
        self.buildings.append(Position((2,4)))
        self.buildings.append(Position((3,2)))
        self.buildings.append(Position((3,4)))
        # Receipts 
        self.receipts = []
        self.receipts.append((Position((0,3)), 1))
        self.receipts.append((Position((2,3)), 0))
        # Delivers
        self.delivers = []
        self.delivers.append((Position((0,0)), 0))
        self.delivers.append((Position((0,6)), 1))


