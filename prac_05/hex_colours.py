"""
CP1404 Practical 5
Hexadecimal colour lookup
"""

COLOUR_CODES = {"AbsoluteZero": "#0048ba", "AcidGreen": "#b0bf1a", "AliceBlue": "#f0f8ff", "Alizarincrimson": "#e32636",
              "Amaranth": "#e52b50", "Amber": "#ffbf00", "Amethyst": "#9966cc", "AntiqueWhite": "	#faebd7",
              "Aqua": "#00ffff", "ArmyGreen": "#4b5320"}

colour_name = input("Enter a hex colour name: ")
while colour_name != "":
    if colour_name in COLOUR_CODES:
        print(colour_name, "is", COLOUR_CODES[colour_name])
    else:
        print("Invalid hex colour")
    colour_name = input("Enter a hex colour name: ")
for item in COLOUR_CODES.items():
    print(f'{item[0]:15} is {item[1]}')
