def convert_to_world(camera, pos):
    # convert from screen coordinates to world coordinates
    world_pos = (camera.position[0]+pos[0], camera.position[1]+pos[1])
    return world_pos

def convert_to_screen(camera, pos):
    # convert from world coordinates to screen coordinates 
    screen_pos = (pos[0]-camera.position[0], pos[1]-camera.position[1])
    return screen_pos

def current_square(camera, pos):
    squarepos = convert_to_world(camera, pos)
    indices = (int(squarepos[0]/camera.boxsize), int(squarepos[1]/camera.boxsize))
    return indices