import random

def generateWorld():
    world = []
    for y in range(60):
        row = []
        for x in range(120):
            if y < 20:
                row.append(["TILE_AIR", [x, y], 0, 0])
            if y >= 20 and y < 40:
                row.append(["TILE_DIRT", [x, y], 1, 1])
            if y >= 40:
                row.append(["TILE_STONE", [x, y], 2.5, 2.5])
        world.append(row)

    y = 19
    x = random.randint(1, 15)
    for row in world:
        for tile in row:
            if tile[1] in [[x, y], [x, y - 1], [x, y - 2], [x, y - 3]]:
                tile = ["TILE_WOOD", tile[1], 1.5, 1.5]

    print(world)
    return world
