import random

def generateWorld():
    world = []
    for y in range(60):
        row = []
        for x in range(160):
            if y < 20:
                row.append(["TILE_AIR", [x, y], 0, 0])
            if y >= 20 and y < 40:
                row.append(["TILE_DIRT", [x, y], 1, 1])
            if y >= 40:
                row.append(["TILE_STONE", [x, y], 2.5, 2.5])
        world.append(row)

    for n in range(random.randint(6, 15)):
        y = 19
        x = random.randint(1, 160)
        for row in range(len(world)):
            for tile in range(len(world[row])):
                if world[row][tile][1] in [[x, y], [x, y - 1], [x, y - 2], [x, y - 3]]:
                    world[row][tile] = ["TILE_WOOD", world[row][tile][1], 1.5, 1.5]
                if world[row][tile][1] in [[x - 1, y - 2], [x + 1, y - 2], [x - 1, y - 3], [x + 1, y - 3], [x - 2, y - 2], [x + 2, y - 2], [x - 2, y - 3], [x + 2, y - 3], [x, y - 4], [x - 1, y - 4], [x + 1, y - 4]]:
                    world[row][tile] = ["TILE_LEAF", world[row][tile][1], 0.25, 0.25]


    return world
