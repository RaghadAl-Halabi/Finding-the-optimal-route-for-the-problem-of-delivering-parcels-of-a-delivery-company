import queue, time, copy

import termcolor


class A_star:
    def __init__(self, state):
        self.state = state
        self.solusionPath = []
        self.visited = []

    def run(self, heuristicNumber):
        t = time.time()
        visited = []
        pqueue = queue.PriorityQueue()
        x = 0
        pqueue.put((0, 0, x, self.state))
        statesCounter = 0

        
        while pqueue:
            element = pqueue.get()
            cost = element[1]
            node = element[3]
            statesCounter += 1 
            
            if node in visited:
                continue

            visited.append(node)
            

            if node.endState():
                solution = []
                p1 = 0
                termcolor.cprint('Execution Time: ' + str(time.time() - t), 'red')
                termcolor.cprint("Visited: " + str(len(visited)), 'green')
                termcolor.cprint("Processed States Number: " + str(statesCounter), 'blue')
                termcolor.cprint("Final Total Cost: " + str(cost), 'yellow')
                
                while node != None:
                    solution.append(node)
                    node = copy.deepcopy(node.parent)
                termcolor.cprint('Moves Number: ' + str(len(solution) - 1 - (len(self.state.delivers) * 2)), 'magenta')
                # while solution:
                #     s1 = solution.pop()
                #     time.sleep(0.8)
                #     s1.show(p1)
                #     p1+=1
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
                         
                    additionalCost = 0
                    x += 1      
                    if(heuristicNumber == 1):
                        additionalCost = total_cost + self.heuristic1(neighbour)
                    elif(heuristicNumber == 2):
                        additionalCost = total_cost + self.heuristic2(neighbour)
                    elif(heuristicNumber == 3):
                        additionalCost = total_cost + self.heuristic3(neighbour)
                    if(heuristicNumber == 4):
                        additionalCost = total_cost + self.heuristic1(neighbour) + self.heuristic2(neighbour) + self.heuristic3(neighbour)
                    
                    add = False 
                    found = False   
                    for v in pqueue.queue:
                        if v[3] == neighbour:
                            found = True
                            if v[1] > total_cost: 
                               add = True
                               pqueue.queue.remove(v)

                    if add or not found:      
                      pqueue.put((additionalCost, total_cost, x, copy.deepcopy(neighbour)))

                    
                    
                   
                   

    def heuristic1(self, state):
        return (abs(state.truck.position.x - state.gridInfo.goalPosition.x) + abs(state.truck.position.y - state.gridInfo.goalPosition.y))

    def heuristic2(self, state):
        totalCost = 0
        for deliver in state.delivers:
            found = False
            for receipt in state.receipts:
                if deliver[1] == receipt[1]:
                    totalCost += (((abs(state.truck.position.x - receipt[0].x) + abs(state.truck.position.y - receipt[0].y)) * 
                                (len(state.truck.parcels) + 1 )) + ((abs(receipt[0].x - deliver[0].x) + abs(receipt[0].y - deliver[0].y)) * 
                                (len(state.truck.parcels) + 2)))
                                
                    found = True
            if not found:
                totalCost += ((abs(state.truck.position.x - deliver[0].x) + abs(state.truck.position.y - deliver[0].y)) * (len(state.truck.parcels)) + 1)
        return totalCost

    def heuristic3(self, state):
        maxCost = 0
        for deliver in state.delivers:
            found = False
            for receipt in state.receipts:
                if deliver[1] == receipt[1]:
                    maxCost += max(maxCost, (((abs(state.truck.position.x - receipt[0].x) + abs(state.truck.position.y - receipt[0].y)) * 
                                (len(state.truck.parcels) + 1)) + ((abs(receipt[0].x - deliver[0].x) + abs(receipt[0].y - deliver[0].y)) * 
                                (len(state.truck.parcels) + 2))))
                                
                    found = True
            if not found:
                maxCost += max(maxCost, ((abs(state.truck.position.x - deliver[0].x) + abs(state.truck.position.y - deliver[0].y)) * (len(state.truck.parcels)))+1)
        return maxCost
