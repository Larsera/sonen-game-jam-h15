
class Tile(self):

    def __init__(self, (au, dc, sc, ic, wc), name):
        self.actions_used = au
        self.danger_chance = dc
        self.shadow_chance = sc
        self.item_chance = ic
        self.water_chance = wc
        self.name = name

# TODO: real values
def get_tile(ident):
    return {0 : Tile((0, 0, 0, 0, 0, 0), "empty desert"),
            1 : Tile((0, 0, 0, 0, 0, 0), "big rock"),
            2 : Tile((0, 0, 0, 0, 0, 0), "small rock"),
            3 : Tile((0, 0, 0, 0, 0, 0), "jagged rock"),
            4 : Tile((0, 0, 0, 0, 0, 0), "oasis"),
            5 : Tile((0, 0, 0, 0, 0, 0), "abandoned camp"),
            6 : Tile((0, 0, 0, 0, 0, 0), "pyramid")}[ident]
