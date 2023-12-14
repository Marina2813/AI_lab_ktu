'''Water Jug Problem is a classic problem in Artificial Intelligence (AI) that involves finding a way to measure specific amounts of water using two jugs with different capacities.
The goal is to reach a specific target amount of water in one of the jugs, without exceeding its capacity, by transferring water from one jug to another.'''

from collections import deque
def water_jug_bfs(jug1_capacity, jug2_capacity, goal):
    visited = set()
    queue = deque([(0, 0, [])])
    while queue:

        jug1, jug2, path = queue.popleft()

        if jug1 == goal or jug2 == goal:
            print("Solution found! Path:", path)
            return
        
        # Fill jug 1
        if jug1 < jug1_capacity:
            new_jug1 = jug1_capacity
            new_jug2 = jug2

            if (new_jug1, new_jug2) not in visited:
                visited.add((new_jug1, new_jug2))
                new_path = path + [(new_jug1, new_jug2)]
                queue.append((new_jug1, new_jug2, new_path))

        # Fill jug 2
        if jug2 < jug2_capacity:
            new_jug1 = jug1
            new_jug2 = jug2_capacity

            if (new_jug1, new_jug2) not in visited:
                visited.add((new_jug1, new_jug2))
                new_path = path + [(new_jug1, new_jug2)]
                queue.append((new_jug1, new_jug2, new_path))

        # Pour from jug 1 to jug 2
        if jug1 > 0 and jug2 < jug2_capacity:
            amount_to_pour = min(jug1, jug2_capacity - jug2)
            new_jug1 = jug1 - amount_to_pour
            new_jug2 = jug2 + amount_to_pour

            if (new_jug1, new_jug2) not in visited:
                visited.add((new_jug1, new_jug2))
                new_path = path + [(new_jug1, new_jug2)]
                queue.append((new_jug1, new_jug2, new_path))

        # Pour from jug 2 to jug 1
        if jug2 > 0 and jug1 < jug1_capacity:
            amount_to_pour = min(jug2, jug1_capacity - jug1)
            new_jug1 = jug1 + amount_to_pour
            new_jug2 = jug2 - amount_to_pour
            
            if (new_jug1, new_jug2) not in visited:
                visited.add((new_jug1, new_jug2))
                new_path = path + [(new_jug1, new_jug2)]
                queue.append((new_jug1, new_jug2, new_path))

    print("No solution found!")

target = int(input('Enter the amount of water to be obtained: '))
jug1_max = int(input('Enter the capacity of Jug 1: '))
jug2_max = int(input('Enter the capacity of Jug 2: '))

water_jug_bfs(jug1_max, jug2_max, target)