import random

def generateWorld():
    world = []
    for y in range(45):
        row = []
        for x in range(65):
            if y < 10:
                row.append(["TILE_AIR", [x, y], 0, 0])
            if y >= 10 and y < 20:
                row.append(["TILE_DIRT", [x, y], 0.5, 0.5])
            if y >= 20:
                row.append(["TILE_STONE", [x, y], 1, 1])
        world.append(row)
    return world