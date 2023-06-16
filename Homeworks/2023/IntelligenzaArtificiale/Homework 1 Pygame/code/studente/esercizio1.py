import math


class Node:

    def __init__(self, state, h, path_cost=0, parent=None):
        self.state = state
        self.h = h
        self.path_cost = path_cost
        self.parent = parent

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
        heuristic_fn
):
    """Implementare l'algoritmo di ricerca A*.

    Parametri:
    - initial_state: posizione (x, y) della cella di partenza
    - goal_test: funzione da usare come goal_test(s), che ritorna
      True se e solo se s è uno stato di goal
    - successor_fn: funzione da usare come successor_fn(s), che ritorna
      una lista di tuple (s1, c) dove s1 è un successore di s, mentre
      c è il costo della transizione da s ad s1
    - heuristic_fn: funzione da usare come heuristic_fn(s), che ritorna
      un valore numerico.
    
    Questa funzione deve ritornare l'ultimo nodo della soluzione (un
    oggetto di tipo Node).
    """
    open_list = []      #Nodi da esplorare
    closed_set = set()  #Insieme per i nodi già esplorati

    print(goal_test)

    if goal_test == (12,4):
        print("Debugga qui")

    if initial_state == (0,7):
        print("Debugga qui")

    initial_node = Node(initial_state, heuristic_fn(initial_state), 0, None)
    open_list.append(initial_node)

    while open_list:

        current_node = min(open_list, key=lambda node: node.path_cost + node.h)
        open_list.remove(current_node)

        if goal_test(current_node.state):
            return current_node

        closed_set.add(current_node.state)

        successors = successor_fn(current_node.state)
        for successor, cost in successors:
            if successor in closed_set:
                continue

            new_path_cost = current_node.path_cost + cost

            #nodo che rappresenta uno stato successore
            new_node = Node(successor, heuristic_fn(successor), new_path_cost, current_node)

            open_node = next((node for node in open_list if node.state == successor), None)
            if open_node and open_node.path_cost <= new_path_cost:
                continue

            open_list.append(new_node)

    return None


def heuristic(s, goal, is_solid):
    """ho scelto un'euristica basata sulla distanza di Manhattan perché è adatta a un grid world in cui
    gli agenti possono muoversi solo in orizzontale e verticale. La distanza di Manhattan fornisce una stima accurata
    del numero minimo di mosse necessarie per raggiungere il goal
    """
    x_s, y_s = s
    x_goal, y_goal = goal
    if is_solid(goal):
        return math.inf
    distance = math.sqrt((x_goal - x_s) ** 2 + (y_goal - y_s) ** 2)
    return distance
