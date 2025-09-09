import game
import os
import bots

def clear():
   os.system("cls" if os.name == "nt" else "clear")

class mainmenu:
    def display_main_menu():
        while True:
            print("hello, welcome to the mafia game, do you want to: \n1.start game. \n2.exit.")
            user_input = input("enter[1,2]: ")
            if user_input == "1".strip():
              clear()
              print("do you want to: \n1.create a normal room. \n2.custom the room.")
              user_input2 = input("enter[1,2]: ")
              if user_input2 == "1".strip():
                 clear()
                 print("which levels do you want to make bots play but this level: \n1.Easy \n2.Medime \n3.hard ")
                 user_input3 = input("enter[1,2,3]: ")
                 if user_input3 == "1".strip():
                    None
                 elif user_input3 == "2".strip():
                    None
                 elif user_input3 == "3".strip():
                    None
                 else:
                    print("invalid input, please try again.")

              elif user_input2 == "2".strip():
                 clear()
                 num_of_mafia = int(input("how many mafia: "))
                 num_of_sheriff = int(input("how many detective: "))
                 num_of_doctor = int(input("how many doctor: "))
                 num_of_innocent = int(input("how many civilians: "))
                 clear()
                 print("which levels do you want to make bots play but this level: \n1.Easy \n2.Medime \n3.hard ")
                 user_input3 = input("enter[1,2,3]: ")
                 if user_input3 == "1".strip():
                    level = "Easy"
                 elif user_input3 == "2".strip():
                    level = "Medime"
                 elif user_input3 == "3".strip():
                    level = "Hard"
                 else:
                    print("invalid input, please try again.")
                 clear()
                 game.game.start_game(level, num_of_mafia, num_of_sheriff, num_of_doctor, num_of_innocent)
        
            elif user_input == "2".strip():
              quit()

            else:
              print("invalid input, please enter 1 to start game and 2 to exit.")
              user_input = input("enter[1,2]: ")