import math


def successors(s, is_solid, region_width, region_height):
    """Implementare le funzioni di successione e costo.

    Parametri:
    - s: stato del quale vanno calcolati i successori e i costi delle
      relative transizioni
    - is_solid: funzione da usare come is_solid(p) che ritorna True
      se e solo se la cella in posizione p è piena
    - region_width: numero di colonne della griglia
    - region_height: numero di righe della griglia

    Questa funzione deve ritornare una lista di tuple (s1, c), dove s1
    è un successore di s, mentre c è il costo della transizione da s
    ad s1.
    """
    actions = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # Azioni: su, giù, sinistra, destra
    successorsList = []

    for action in actions:
        dx, dy = action
        x, y = s[0] + dx, s[1] + dy

        # Verifica se il successore è all'interno dei limiti della griglia
        if 0 <= x < region_width and 0 <= y < region_height:
            #Se la cella non è piena la aggiungo alla lista con un cost di transizione standard, altrimenti
            #la aggiungo con un costo pari a 5, scelto arbitrariamente per favorire i percorsi senza celle piene
            if not is_solid((x, y)):
                successorsList.append(((x, y), 1))
            else:
                successorsList.append(((x, y), 5))

    return successorsList


def heuristic(s, goal, is_solid, region_width, region_height):
    """ho scelto un'euristica basata sulla distanza di Manhattan pesata perché tiene conto anche del numero di celle
    piene lungo il percorso. Questo permette di trovare un percorso ottimale che minimizza sia il numero di mosse
    necessarie che il numero di celle piene incontrate, anche quando non è possibile raggiungere il goal.
    """
    # Calcola la distanza Euclidea tra lo stato corrente e il goal
    distance = math.sqrt((goal[0] - s[0]) ** 2 + (goal[1] - s[1]) ** 2)

    # Calcola il numero di celle piene nel percorso
    solid_cells = sum(1 for x in range(region_width) for y in range(region_height) if is_solid((x, y)))

    # Calcola l'euristica considerando la distanza e il numero di celle piene
    penalty = 8
    heuristic_value = distance + penalty * solid_cells

    return heuristic_value

