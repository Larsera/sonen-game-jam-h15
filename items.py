
class weapon():

    def __init__(self, name, dmg=1):
        self.name = name
        self.dmg = dmg

class item_hydration():

    def __init__(self, name, hdr):
        self.name = name
        self.hydration = hdr

class item_foodstuff():

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

class item_medicin():

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
