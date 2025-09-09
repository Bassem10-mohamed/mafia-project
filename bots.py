import random
import players

class bot(players.player):
    def __init__(self, name, role):
        super().__init__(name, role)
        self.name = self.generate_bot_name()
        self.role = self.assign_role()

    def generate_bot_name(self):
        bot_names = ["Bot_Alice", "Bot_Bob", "Bot_Charlie", "Bot_Dave", "Bot_Eve"]
        return random.choice(bot_names)

    def assign_role(self):
        roles = ["Mafia", "Doctor", "Detective", "Civilian"]
        return random.choice(roles)
