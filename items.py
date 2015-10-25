
class weapon():


    def __init__(self, name, dmg=1, rarity=1):
        self.name = name
        self.dmg = dmg
        self.rarity = rarity

def get_weapon(ident):
    return {"stick" : weapon("Stick", rarity=2),
        "sharp_rock" : weapon("Sharp Rock", dmg=2, rarity=4),
        "pointy_stick" : weapon("Pointy Stick", dmg=3, rarity=6),
        "plusone_mace" : weapon("+1 Mace", dmg=4, rarity=8),
        "warped_blade" : weapon("Warped Blade", dmg=5, rarity=10)}.get(ident)

class item_hydration():

    def __init__(self, name, hdr, rarity=1):
        self.name = name
        self.hydration = hdr
        self.rarity = rarity

def get_water(ident):
    return {"water_bottle" : item_hydration("Water Bottle", 80)}.get(ident)

class item_foodstuff():

    def __init__(self, name, amount, hdr, rarity=1):
        self.name = name
        self.amount = amount
        self.hdr = hdr
        self.rarity = rarity

def get_foodstuff(ident):
    return {"raw_meat" : item_foodstuff("Raw meat", 40, 0),
            "cactus_piece" : item_foodstuff("Cactus piece", 30, 20),
            "granola_bar" : item_foodstuff("Granola bar", 50, 0)}.get(ident)


class item_medicine():

    def __init__(self, name, hp_restore=0, antidote=False, hydration=0, hunger=0, rarity=1):
        self.name = name
        self.hprestore = hp_restore
        self.antidote = antidote
        self.hydration = hydration
        self.hunger = hunger
        self.rarity = rarity

def get_medicine(ident):
    return item_medicine("Antidote", antidote=True)

