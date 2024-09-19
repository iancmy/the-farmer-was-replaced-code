def ymove(pos_y, x_direction=None, y_direction=None):
    if y_direction == North:
        if pos_y == get_world_size() - 1:
            next = xmove(get_pos_x(), x_direction, y_direction)
            return next, South
        else:
            move(North)
            return x_direction, North
    elif y_direction == South:
        if pos_y == 0:
            next = xmove(get_pos_x(), x_direction, y_direction)
            return next, North
        else:
            move(South)
            return x_direction, South
    else: 
        if pos_y < get_world_size() // 2:
            move(North)
            return x_direction, North
        else:
            move(South)
            return x_direction, South

def xmove(pos_x, x_direction=None, y_direction=None):
    if x_direction == East:
        if pos_x == get_world_size() - 1:
            return West
        else:
            move(East)
            return East
    elif x_direction == West:
        if pos_x == 0:
            return East
        else:
            move(West)
            return West
    else: 
        if pos_x < get_world_size() // 2:
            return East
        else:
            return West
