import random

def generateWorld():
    world = []
    for y in range(60):
        row = []
        for x in range(120):
            if y < 20:
                row.append(["TILE_AIR", [x, y], 0, 0])
            if y >= 20 and y < 40:
                row.append(["TILE_DIRT", [x, y], 0.5, 0.5])
            if y >= 40:
                row.append(["TILE_STONE", [x, y], 1, 1])
        world.append(row)
    return world
