def queensAttack(n, k, r_q, c_q, obstacles):
    '''
    n: dimension of board
    k: num obstacles, can be ignored
    r_q: queen row
    c_q: queen column
    obstacles: coordinates of obstables (row,column)
    '''

    queens_attacks = get_all_the_queens_attacks(n, r_q, c_q)

    reduce_the_queens_attacks_with_any_obstacles(r_q, c_q, queens_attacks, obstacles)

    return sum(queens_attacks.values())

def get_all_the_queens_attacks(n, r_q, c_q):
    return {
        "n"  : (r_q - 1),
        "s"  : (n - r_q),
        "e"  : (n - c_q),
        "w"  : (c_q - 1),
        "nw" : min(r_q-1, c_q-1),
        "ne" : min(r_q-1, n-c_q),
        "se" : min(n-r_q, n-c_q),
        "sw" : min(n-r_q, c_q-1)
    }

def reduce_the_queens_attacks_with_any_obstacles(r_q, c_q, queens_attacks, obstacles):
    for obstacle in obstacles:
        direction = get_direction_of_obstacle(obstacle, r_q, c_q)
        
        obstacle_not_in_path_of_attack = True if direction is None else False
        if obstacle_not_in_path_of_attack:
            continue
        
        reduced_attack_amount = calculate_reduced_attack_amount(obstacle, r_q, c_q)
        queens_attacks[direction] = min(queens_attacks[direction], reduced_attack_amount)

def get_direction_of_obstacle(obstacle, r_q, c_q):
    if is_obstacle_in_horizontal_path_of_attack(obstacle, r_q):
        if obstacle[1] < c_q:
            return "w"
        else:
            return "e"
    elif is_obstacle_in_vertical_path_of_attack(obstacle, c_q):
        if obstacle[0] < r_q:
            return "n"
        else:
            return "s"
    elif is_obstacle_in_diagonal_path_of_attack(obstacle, r_q, c_q):
        if obstacle[0] < r_q and obstacle[1] < c_q:
            return "nw"
        elif obstacle[0] < r_q and obstacle[1] > c_q:
            return "ne"
        elif obstacle[0] > r_q and obstacle[1] > c_q:
            return "se"
        else:
            return "sw"
    
    return None

def calculate_reduced_attack_amount(obstacle, r_q, c_q):
    return max(abs(c_q - obstacle[1]), abs(r_q - obstacle[0])) - 1

def is_obstacle_in_horizontal_path_of_attack(obstacle, r_q):
    return (obstacle[0] == r_q)

def is_obstacle_in_vertical_path_of_attack(obstacle, c_q):
    return (obstacle[1] == c_q)

def is_obstacle_in_diagonal_path_of_attack(obstacle, r_q, c_q):
    return abs(obstacle[0] - r_q) == abs(obstacle[1] - c_q)

