"""
CP1404/CP5632 Practical
Hex colour
"""

HEX_COLOUR = {"AbsoluteZero": "#0048ba", "AcidGreen": "#b0bf1a", "AliceBlue": "#f0f8ff", "Alizarincrimson": "#e32636",
              "Amaranth": "#e52b50", "Amber": "#ffbf00", "Amethyst": "#9966cc", "AntiqueWhite": "	#faebd7",
              "Aqua": "#00ffff", "ArmyGreen": "#4b5320"}

colour = input("Enter hex colour: ")
while colour != "":
    if colour in HEX_COLOUR:
        print(colour, "is", HEX_COLOUR[colour])
    else:
        print("Invalid hex colour")
    colour = input("Enter hex colour: ")
for item in HEX_COLOUR.items():
    print(f'{item[0]:15} is {item[1]}')
