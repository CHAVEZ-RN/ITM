def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.'''
    if to_member in social_graph[from_member]["following"] and from_member in social_graph[to_member]["following"]:
        return "friends"
    elif to_member in social_graph[from_member]["following"]:
        return "follower"
    elif from_member in social_graph[to_member]["following"]:
        return "followed by"
    else:
        return "no relationship"


def tic_tac_toe(board):
    '''Tic Tac Toe.'''
    size = len(board)

    # TO Check rows
    for row in board:
        if row.count(row[0]) == size and row[0] != "":
            return row[0]

    # TO Check columns
    for col in range(size):
        col_vals = [board[row][col] for row in range(size)]
        if col_vals.count(col_vals[0]) == size and col_vals[0] != "":
            return col_vals[0]

    # TO Check diagonals
    diag1 = [board[i][i] for i in range(size)]
    if diag1.count(diag1[0]) == size and diag1[0] != "":
        return diag1[0]

    diag2 = [board[i][size - 1 - i] for i in range(size)]
    if diag2.count(diag2[0]) == size and diag2[0] != "":
        return diag2[0]

    return "NO WINNER"


def eta(first_stop, second_stop, route_map):
    '''ETA.'''
    total_time = 0
    current_stop = first_stop

    while current_stop != second_stop:
        for (start, end), leg in route_map.items():
            if start == current_stop:
                total_time += leg["travel_time_mins"]
                current_stop = end
                break
    return total_time
