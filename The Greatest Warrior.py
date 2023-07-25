class Warrior:
    RANKS = ["Pushover", "Novice", "Fighter", "Warrior", "Veteran",
             "Sage", "Elite", "Conqueror", "Champion", "Master", "Greatest"]

    def __init__(self):
        self.level = 1
        self.experience = 100
        self.rank = "Pushover"
        self.achievements = []

    def battle(self, enemy_level):
        if enemy_level not in range(1, 101):
            return "Invalid level"

        diff = enemy_level - self.level
        if diff <= -2:
            self.experience += 0
            return "Easy fight"
        elif diff == -1:
            self.experience += 5
            return "A good fight"
        elif diff == 0:
            self.experience += 10
            return "A good fight"
        elif diff >= 1 and diff <= 2:
            exp = 20 * diff * diff
            self.experience += exp
            return "An intense fight"
        elif diff > 2:
            self.experience += 0
            return "An intense fight"
        else:
            return "You've been defeated"

        self._check_level()

    def _check_level(self):
        if self.level < 100:
            while self.experience >= 100 * self.level:
                self.experience -= 100 * self.level
                self.level += 1
                self._check_rank()
        else:
            self.experience = 10000

    def _check_rank(self):
        rank_idx = (self.level - 1) // 10
        self.rank = self.RANKS[rank_idx]

    def training(self, training_data):
        desc, exp, min_level = training_data
        if self.level >= min_level:
            self.experience += exp
            self.achievements.append(desc)
            self._check_level()
            return desc
        else:
            return "Not strong enough"
