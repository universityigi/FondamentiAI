import heapq
class Node:

    def __init__(self, state, h, path_cost=0, parent=None):
        self.state = state
        self.h = h
        self.path_cost = path_cost
        self.parent = parent

    #method added to use priority queues correctly
    def __lt__(self, other):
        return (self.path_cost + self.h) < (other.path_cost + other.h)

    def to_solution(self):
        seq = []
        node = self
        s0 = None
        while node is not None:
            if node.parent is None:
                s0 = node.state
            if node.parent is not None:
                seq.append(node.state)
            node = node.parent
        assert s0 is not None
        return list(reversed(seq))
    
    def __repr__(self):
        s = f'Node(state={self.state}, path_cost={self.path_cost}'
        s += ')' if self.parent is None else f', parent={self.parent.state})'
        return s


def a_star(
    initial_state,
    goal_test,
    successor_fn,
    heuristic_fn):
    """
    Implements the A* search algorithm.

    Args:
        initial_state: the initial state of the problem
        goal_test: a function that returns True if the given state is a goal state, and False otherwise
        successor_fn: A list of (action, next_state, cost) tuples representing the possible successor states, the actions that lead to
                      them, and the cost of taking those actions
        heuristic_fn: a function that takes a state as input and returns Returns the Manhattan distance from the current state to the goal state.

    Returns:
        The goal Node containing the optimal path from the initial state to the goal state
    """
    # Initialize the start node
    start_node = Node(initial_state, heuristic_fn(initial_state))
    start_node.f = start_node.h + start_node.path_cost
    # Initialize the priority queue with the start node and it's f value
    q = [(start_node.f, start_node)]
    # Initialize the set of explored nodes
    explored = set()

    # While the priority queue is not empty
    while q:
        # Get the node with the lowest f(n) value from the priority queue
        _, current_node = heapq.heappop(q)
        # If the current node is a goal state, return it
        if goal_test(current_node.state):
            return current_node
        # If the current node has already been explored, skip it
        if current_node.state not in explored:
            #set the current node to explored
            explored.add(current_node.state)
            # Generate the successors of the current state
            for action, next_state, cost in successor_fn(current_node.state):
                # Create the successor node
                h = heuristic_fn(next_state) 
                g = current_node.path_cost + cost
                successor_node = Node(next_state, h, g, current_node)
                successor_node.f = successor_node.h + successor_node.path_cost
                # Add the successor node to the priority queue
                heapq.heappush(q, (successor_node.f, successor_node))

    # If no goal state was found, return None
    return None

def successors(s, is_solid, region_width, region_height):
    """
    Generates the successors of a given state.

    Returns:
        A list of (action, next_state, cost) tuples representing the possible successor states, the actions that lead to
        them, and the cost of taking those actions
    """
    #obtain coordinates of current state
    x, y = s
    successors = []
    #for each direction
    for i, j , a in [(-1, 0, 'W'), (0, -1, 'S'), (1, 0, 'E'), (0, 1, 'N')]:
        nx, ny = x + i, y + j
        #check if the new state is valid, if yes add it to the successors
        if 0 <= nx < region_width and 0 <= ny < region_height:
            successors.append((a, (nx, ny), 1))
    return successors

def heuristic(s, goal, is_solid):
    """
    Returns the Manhattan distance from the current state to the goal state.
    """

    #otherwise return the manhattan distance
    h = abs(s[0] - goal[0]) + abs(s[1] - goal[1])

    #if the current state is a solid state, return infinity
    if is_solid(s):
        return h+1000
    
    return h