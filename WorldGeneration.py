import random

def generateWorld():
    world = []
    for y in range(45):
        row = []
        for x in range(65):
            if y < 10:
                row.append(["TILE_AIR"])
            if y >= 10 and y < 20:
                row.append(["TILE_DIRT"])
            if y >= 20:
                row.append(["TILE_STONE"])
        world.append(row)
    return world
