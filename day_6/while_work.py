def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jamp_wall():
    if front_is_clear() and right_is_clear():
        turn_right()
        while front_is_clear():
            move()
    elif wall_in_front() and wall_on_right():
        turn_left()
        while front_is_clear():
            move()
    elif wall_in_front() and right_is_clear():
        turn_right()
        while front_is_clear():
            move()
            if front_is_clear() and right_is_clear():
                if front_is_clear():
                    turn_right()
                    while front_is_clear():
                        move()
                if wall_in_front():
                    turn_left()
                    while front_is_clear():
                        move()


while not at_goal():
    if wall_in_front():
        jamp_wall()
    else:
        move()