import random

class player:
    def __init__(self, name, role):
        self.name = self.choose_name
        self.role = self.choose_role

    def choose_name(self):
        name = input("Enter your name: ")
        name = self.name
        return name

    def choose_role(self):
        roles = ["Mafia", "Doctor", "Detective", "Civilian"]
        return random.choice(roles)

    def display_info(self):
        print(f"Player Name: {self.name}, Role: {self.role}")
        
        