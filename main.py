# Initiaizing the graph with the cities and distances
class Graph:
    # init method or constructor
    def __init__(self):
        self.graph = dict() # creating a dictionary

    # adding the edge and its cost(distance)
    def add_edge(self, node1, node2, cost):
        if node1 not in self.graph:
            self.graph[node1] = []
        if node2 not in self.graph:
            self.graph[node2] = []
        
        self.graph[node1].append((node2, int(cost)))

# Checking about the charging and updating the list with the cities to be halted 
class Charging():
    # init method or constructor
    def __init__(self, Capacity):
        self.Capacity = Capacity # capacity of the vehicle
        self.output = []

    # find the charging stations
    def findChargingStations(self, init_graph):
        initial_mileage = self.Capacity
        starting_city = list(init_graph.graph.items())[0][0] # get the starting city
        self.output.append(starting_city) # append the starting city to the list

        for current_city, val in init_graph.graph.items():
            miles_to_next_city = val[0][1] # get the miles it needs to travel to the next city
            # Check if it can travel back incase a city is broken
            if not ((initial_mileage - 2 * miles_to_next_city) >0):
                self.output.append(current_city)
                initial_mileage = self.Capacity
            elif miles_to_next_city == 0: #destination city
                self.output.append(current_city)
            initial_mileage = initial_mileage - miles_to_next_city

        # rturn the final list of cities to be halted
        return self.output

def main():
    # Create a empty graph
    inital_graph = Graph()

    # Read the input - capacity
    while True:
        try: 
            Capacity = int(input("Enter C: "))
        except ValueError:
            print("C needs to be an integer, please re-enter C")
            continue
        if Capacity <= 250 or Capacity >= 350:
            print("C is out of range, please re-enter C")
            continue
        else:
            break
    
    # Read the input - number of cities(n)
    while True:
        try:
            n = int(input("Enter how many cities (n): "))
        except ValueError:
            print('n needs to be an integer, please re-enter n')
            continue
        if n > 3 and n < 20:
            break
        else:
            print('n is out of range, please re-enter n')
            continue
    
    destination = ''
    # Read the cities and the distance between them
    print("Enter current city, next city, distance. Seprate by space: ")
    for iterator in range(int(n) - 1):
        while True:
            try:
                city1, city2, dist = input().split()
                dist=int(dist)
            except ValueError:
                print('distance needs to be an integer, please re-enter the current city, next city, distance. Seprate by space: ')
                continue
            if int(dist) <= 10 or int(dist) >= int(Capacity)/2:
                print('Distance is not valid, please re-enter input')
                continue
            elif city1 is not destination:
                if (destination == ''):
                    break
                else:
                    print(f'Starting city needs to be {destination}, please re-enter input')
                    continue
            else:
                break
        
        # Adding the edges to a graph with the distances given
        inital_graph.add_edge(city1, city2, dist)
        destination = city2
        if  iterator != int(n)-2:
            print('Enter next input: ')
        else:
            print('List of cities to halt: ')

    inital_graph.add_edge(destination, destination, 0)
    # Initializing the capacity
    obj = Charging(int(Capacity))
    # Call the function to find the charging stations 
    result = obj.findChargingStations(inital_graph)
    print(result)

if __name__=="__main__":
    main()
