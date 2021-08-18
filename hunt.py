print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

choice1= input("You are at a crossroad, enter 'left' or 'right' to continue: \n")
choice1=choice1.lower()
if choice1 == "right":
  print("you stepped on a bear trap and dies, game over")
elif choice1 == "left":
  print("Good choice, you avoided the trap and reached a river \n")
  choice2 = input("You are at the river, choose to 'swim' or 'wait' \n")
  choice2=choice2.lower()
  if choice2 =="swim":
    print("you were eaten by an alligator, game over")
  elif choice2=="wait":
    print("You waited for a while and a rowboat appeared, it offers you to take you to a cave\n")
    choice3=input("You have reached the cave and see three doors, choose between 'red', 'blue', or 'yellow' to continue\n")
    choice3=choice3.lower() 
    if choice3=="blue":
      print("You opened the blue door and got eaten by a beast, game over!")
    elif choice3=="red":
      print("you opened the red door and fell into a fiery pit and got burnt to death. Game over!")
    elif choice3== "yellow":
      print("You slowly open the yellow door, and see a treasure chest. It is filled with gold, You win!")
    else:
      print("Ahh soo close, but you lost. Game Over")       
  else:
    print("That seems to be a bad idea, Game over pal!")
else:
  print("Well you dont follow instructions, game over!")    
