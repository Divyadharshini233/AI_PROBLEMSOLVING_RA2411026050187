import itertools

def calculate_distance(route, dist_matrix):
    total = 0
    for i in range(len(route) - 1):
        total += dist_matrix[route[i]][route[i+1]]
    total += dist_matrix[route[-1]][route[0]]
    return total

def brute_force_tsp(dist_matrix):
    n = len(dist_matrix)
    cities = list(range(n))
    min_route = None
    min_distance = float('inf')

    for perm in itertools.permutations(cities):
        distance = calculate_distance(perm, dist_matrix)
        if distance < min_distance:
            min_distance = distance
            min_route = perm

    return min_route, min_distance
