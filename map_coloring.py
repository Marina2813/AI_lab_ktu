'''color = ['Red', 'Blue','Green']
states = ['wa','nt','sa','q','t','v']
neighbour = {}
neighbour['wa'] = ['nt','sa']
neighbour['nt'] = ['wa','sa','q']
neighbour['sa'] = ['nt','wa','q','v']
neighbour['q'] = ['nt','sa','v']
neighbour['v'] = ['q','sa']
neighbour['t'] = []
'''
colors = input("Enter the Colors separated by spaces: ").split()
states = input("Enter the states separated by spaces: ").split()

neighbors = {}
color_of_state = {}

for state in states:
    neighbor_list = input(f"Enter the neighbours of {state} separated by spaces (or leave empty for no neighbors): ").split()
    neighbors[state] = neighbor_list

def promising(state,color):
    #checks if particular color assignment to  a state is valid based on colors assigned to neighbours
    for neighbor in neighbors.get(state):
        color_of_neighbour = color_of_state.get(neighbor)
        if color_of_neighbour == color:
            return False
    return True 

def get_color_of_state(state):
    for color in colors:
        if promising(state,color):
            return color
        
def main():
    for state in states:
        color_of_state[state] = get_color_of_state(state)
    print(color_of_state)

main()