
class weapon():


    def __init__(self, name, dmg=1):
        self.name = name
        self.dmg = dmg

def get_weapon(ident):
    return {"stick" : weapon("Stick"),
        "sharp_rock" : weapon("Sharp rock", dmg=2),
        "pointy_stick" : weapon("Pointy stick", dmg=3),
        "plusone_mace" : weapon("+1 Mace", dmg=4),
        "warped_blade" : weapon("Warped blade", dmg=5)}.get(ident)

class item_hydration():

    def __init__(self, name, hdr):
        self.name = name
        self.hydration = hdr

def get_water(ident):
    return {"water_bottle" : item_hydration("Water Bottle", 80)}.get(ident)

class item_foodstuff():

    def __init__(self, name, amount, hdr):
        self.name = name
        self.amount = amount
        self.hdr = hdr

def get_foodstuff(ident):
    return {"raw_meat" : item_foodstuff("Raw meat", 40, 0),
            "cactus_piece" : item_foodstuff("Cactus piece", 30, 20),
            "granola_bar" : item_foodstuff("Granola bar", 50, 0)}.get(ident)


class item_medicine():

    def __init__(self, name, hp_restore=0, antidote=False, hydration=0, hunger=0):
        self.name = name
        self.hprestore = hp_restore
        self.antidote = antidote
        self.hydration = hydration
        self.hunger = hunger

def get_medicine(ident):
    return {"antidote" : item_medicine("Antidote", antidote=True)

class item_junk():

    def __init__(self, name, bonus):
        self.name = name
        self.bonus = bonus
