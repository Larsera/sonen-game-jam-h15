
class weapon():

   TYPE = {"stick" : Weapon("Stick", desc="A thin stick. Not very effective."),
            "sharp_rock" : Weapon("Sharp rock", dmg=2, 
                desc="Better than a stick, but you have to get too close for comfort."),
            "pointy_stick" : Weapon("Pointy stick", dmg=3,
                desc="A sharpened stick. Perfect for poking things."),
            "plusone_mace" : Weapon("+1 Mace", dmg=4,
                desc="A bottle of mace."),
            "warped_blade" : Weapon("Warped blade", dmg=5,
                desc="Not to be confused with the Vorpal blade.")
            }

    def __init__(self, name, dmg=1, desc=""):
        self.name = name
        self.dmg = dmg
        self.desc = desc

class item_hydration():

    def __init__(self, name, hdr):
        self.name = name
        self.hydration = hdr

class item_foodstuff():

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

class item_medicine():

    def __init__(self, name, hp_restore=0, antidote=False, hydration=0, hunger=0):
        self.name = name
        self.hprestore = hp_restore
        self.antidote = antidote
        self.hydration = hydration
        self.hunger = hunger

class item_junk():

    def __init__(self, name, bonus):
        self.name = name
        self.bonus = bonus
