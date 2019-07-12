def queensAttack(n, k, r_q, c_q, obstacles):
    '''
    n: dimension of board
    k: num obstacles, can be ignored
    r_q: queen row
    c_q: queen column
    obstacles: coordinates of obstables (row,column)
    '''

    filtered_obstacles = cleanup_obstacles(r_q, c_q, obstacles)

    number_of_horizontal_attacks = calculate_number_of_horizontal_attacks(n, r_q, c_q, filtered_obstacles)
    number_of_vertical_attacks = calculate_number_of_vertical_attacks(n, r_q, c_q, filtered_obstacles)
    number_of_forward_diagonal_attacks = calculate_number_of_forward_diagonal_attacks(n, r_q, c_q, filtered_obstacles)
    number_of_backward_diagonal_attacks = calculate_number_of_backwards_diagonal_attacks(n, r_q, c_q, filtered_obstacles)
    
    return number_of_horizontal_attacks + number_of_vertical_attacks + number_of_forward_diagonal_attacks + number_of_backward_diagonal_attacks

def cleanup_obstacles(r_q, c_q, obstacles):
    filtered_obstacles = {}
    for coordinates in obstacles:
        if coordinates[0] == r_q:
            if coordinates[1] < c_q:
                try:
                    if filtered_obstacles["min_w"][1] < coordinates[1]:
                        filtered_obstacles["min_w"] = coordinates
                except KeyError:
                    filtered_obstacles["min_w"] = coordinates
            elif coordinates[1] > c_q:
                try:
                    if filtered_obstacles["min_e"][1] > coordinates[1]:
                        filtered_obstacles["min_e"] = coordinates
                except KeyError:
                    filtered_obstacles["min_e"] = coordinates
        elif coordinates[1] == c_q:
            if coordinates[0] < r_q:
                try:
                    if filtered_obstacles["min_n"][0] < coordinates[0]:
                        filtered_obstacles["min_n"] = coordinates
                except KeyError:
                    filtered_obstacles["min_n"] = coordinates
            elif coordinates[0] > r_q:
                try:
                    if filtered_obstacles["min_s"][0] > coordinates[0]:
                        filtered_obstacles["min_s"] = coordinates
                except KeyError:
                    filtered_obstacles["min_s"] = coordinates 
        elif is_obstacle_in_diagonal_path_of_attack(coordinates, r_q, c_q):
            if coordinates[0] < r_q and coordinates[1] < c_q:
                # nw
                try:
                    if (r_q - coordinates[0]) < (r_q - filtered_obstacles["min_nw"][0]) \
                            and (c_q - coordinates[1]) < (c_q - filtered_obstacles["min_nw"][1]):
                        filtered_obstacles["min_nw"] = coordinates
                except KeyError:
                    filtered_obstacles["min_nw"] = coordinates
            elif coordinates[0] < r_q and coordinates[1] > c_q:
                # ne
                try:
                    if (r_q - coordinates[0]) < (r_q - filtered_obstacles["min_ne"][0]) \
                            and (coordinates[1] - c_q) < (filtered_obstacles["min_ne"][1] - c_q):
                        filtered_obstacles["min_ne"] = coordinates
                except KeyError:
                    filtered_obstacles["min_ne"] = coordinates
            elif coordinates[0] > r_q and coordinates[1] < c_q:
                # sw
                try:
                    if (coordinates[0] - r_q) < (filtered_obstacles["min_sw"][0] - r_q) \
                            and (c_q - coordinates[1]) < (c_q - filtered_obstacles["min_sw"][1]):
                        filtered_obstacles["min_sw"] = coordinates
                except KeyError:
                    filtered_obstacles["min_sw"] = coordinates
            elif coordinates[0] > r_q and coordinates[1] > c_q:
                # se
                try:
                    if (coordinates[0] - r_q) < (filtered_obstacles["min_se"][0] - r_q) \
                            and (coordinates[1] - c_q) < (filtered_obstacles["min_se"][1] - c_q):
                        filtered_obstacles["min_se"] = coordinates
                except KeyError:
                    filtered_obstacles["min_se"] = coordinates

    return filtered_obstacles

def is_obstacle_in_diagonal_path_of_attack(coordinates, r_q, c_q):
    return abs(coordinates[0] - r_q) == abs(coordinates[1] - c_q)

def calculate_number_of_horizontal_attacks(n, r_q, c_q, filtered_obstacles):
    obstacle_factor = 0
    if "min_w" in filtered_obstacles:
        obstacle_factor += filtered_obstacles["min_w"][1]
    if "min_e" in filtered_obstacles:
        obstacle_factor += n-filtered_obstacles["min_e"][1] + 1

    return (n - 1) - obstacle_factor

def calculate_number_of_vertical_attacks(n, r_q, c_q, filtered_obstacles):
    obstacle_factor = 0
    if "min_n" in filtered_obstacles:
        obstacle_factor += filtered_obstacles["min_n"][0]
    if "min_s" in filtered_obstacles:
        obstacle_factor += n-filtered_obstacles["min_s"][0] + 1

    return (n - 1) - obstacle_factor

def calculate_number_of_forward_diagonal_attacks(n, r_q, c_q, filtered_obstacles):
    num_up = min(r_q-1, n-c_q)
    num_down = min(n-r_q, c_q-1)
    
    obstacle_factor = 0
    if "min_ne" in filtered_obstacles:
        obstacle_factor += min(filtered_obstacles["min_ne"][0]-1, n-filtered_obstacles["min_ne"][1]) + 1
    if "min_sw" in filtered_obstacles:
        obstacle_factor += min(n-filtered_obstacles["min_sw"][0], filtered_obstacles["min_sw"][1]-1) + 1

    return num_up + num_down - obstacle_factor

def calculate_number_of_backwards_diagonal_attacks(n, r_q, c_q, filtered_obstacles):
    num_up = min(r_q-1, c_q-1)
    num_down = min(n-r_q, n-c_q)

    obstacle_factor = 0
    if "min_nw" in filtered_obstacles:
        obstacle_factor += min(filtered_obstacles["min_nw"][0]-1, filtered_obstacles["min_nw"][1]-1) + 1
    if "min_se" in filtered_obstacles:
        obstacle_factor += min(n-filtered_obstacles["min_se"][0], n-filtered_obstacles["min_se"][1]) + 1

    return num_up + num_down - obstacle_factor

