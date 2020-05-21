class Pokemon:

    def __init__(self, name, level, type1, type2):
        self.name = name
        self.level = level
        self.type1 = type1
        self.type2 = type2
        self.attacks = []
        self.stats = {}
        self.baseStats = {}
        self.ev = {}
        self.iv = {}
        self.current_status = 0
        self.current_hp = 0

    def compute_stats(self):
        pass

    def compute_standard_stat(self):
        pass

    def compute_hp_stat(self):
        pass


class Attack:

    def __init__(self, name, t, category, pp, power, accuracy):
        self.name = name
        self.type = t
        self.category = category
        self.pp = pp
        self.power = power
        self.accuracy = accuracy
