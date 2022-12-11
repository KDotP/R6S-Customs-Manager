import random as rand
from tkinter import *
import tkinter

# Lists of potential bans, tactics, maps, etc
atk_operators = ["Sledge", "Thatcher", "Ash", "Thermite", "Twitch", "Montagne", "Glaz", "Fuze", "Blitz", "IQ", "Buck", "Blackbeard", "Capitao", "Hibana", "Jackel", "Zofia", "Dokkaebi", "Lion", "Finka", "Maverick", "Nomad", "Gridlock", "Nokk", "Amaru", "Kali", "Iana", "Ace", "Zero", "Flores", "Osa", "Sens", "Grim"]
def_operators = ["Smoke", "Mute", "Castle", "Pulse", "Doc", "Rook", "Kapkan", "Tachanka", "Jager", "Bandit", "Frost", "Valkyrie", "Caveira", "Echo", "Mira", "Lesion", "Ela", "Vigil", "Maestro", "Alibi", "Clash", "Kaid", "Mozzie", "Warden", "Goyo", "Wamai", "Oryx", "Meslusi", "Aruni", "Thunderbird", "Thorn", "Azami", "Solis"]
maps = ["Nighthaven Labs", "Stadium", "Emerald Plains", "Bank", "Border", "Chalet", "Clubhouse", "Coastline", "Consulate", "Favela", "Fortress", "Hereford Base", "House", "Kafe Dostoyevsky", "Kanal", "Oregon", "Outback", "Presidential Plain", "Skyscraper", "Theme Park", "Tower", "Villa", "Yacht"]
atk_strats = []
def_strats = []
rules = []

# Number of bans and playable maps
#atk_bans = 4
#def_bans = 4
#max_playable_maps = 5

# Maximum number of symetric operator bans
max_op_bans = 0
if len(atk_operators) != len(def_operators):
    max_op_bans = len(atk_operators) - 1
else:
    # Set max bans to the lower number of max operators
    if len(atk_operators) < len(def_operators):
        max_op_bans = len(atk_operators) - 1
    else:
        max_op_bans = len(def_operators) - 1

max_maps = len(maps) - 1

# Generate the list of bans
def Generate(gen_atk, gen_def, gen_maps):
    new_atk_bans = rand.sample(atk_operators, gen_atk)
    new_def_bans = rand.sample(def_operators, gen_def)
    playable_maps = rand.sample(maps, gen_maps)

    return new_atk_bans, new_def_bans, playable_maps

# Testing function, gets data directly without keep it within bounds, and reads into terminal
def RunIt():
    atk_bans = int(Entry.get(E1))
    def_bans = atk_bans
    max_playable_maps = int(Entry.get(E2))
    
    # Convert function to variables
    banned_attackers, banned_defenders, available_maps = Generate(atk_bans, def_bans, max_playable_maps)
    print("Banned Attackers: " +  ', '.join(banned_attackers) + "\nBanned Defenders: " + ', '.join(banned_defenders) + "\nAvailable Maps: " + ', '.join(available_maps))


# Get data from user input fields
def GetData():

    atk_bans = int(Entry.get(E1))

    # Keep bans with range
    if atk_bans > max_op_bans:
        atk_bans = max_op_bans
    elif atk_bans < 0:
        atk_bans = 0

    # This application was built with asymmetric operator bans in mind, but now the entrie thing is built around this. My bad.
    def_bans = atk_bans

    # Get maps and ensure numbers are within bounds
    max_playable_maps = int(Entry.get(E2))
    if max_playable_maps < 1:
        max_playable_maps = 1
    elif max_playable_maps > max_maps:
        max_playable_maps = max_maps

    # Return values (order important)
    return atk_bans, def_bans, max_playable_maps

# Create a new window showing the results of the randomizer
def ResultPopup():
    try:
        # Seperate data because it seems to throw an error when passed directly
        # BECAUSE WHO DOESN'T LOVE PYTHON
        atk_ban_max, def_ban_max, playable_map_max = GetData()
        atk_bans, def_bans, playable_maps = Generate(atk_ban_max, def_ban_max, playable_map_max)

        # Create new result window and define size
        newWindow = Toplevel(top)
        newWindow.title("Results")
        newWindow.geometry("750x120")

        # Display for Attacker Bans
        Label(newWindow, text="Banned Attackers:\n" + ', '.join(atk_bans)).pack()

        # Display for Defender Bans
        Label(newWindow, text="Banned Defenders:\n" + ', '.join(def_bans)).pack()

        # Display for Maps
        Label(newWindow, text="Map Choices:\n" + ', '.join(playable_maps)).pack()
    except:
        # Throw error window is invalid input is put
        ErrorPopup()

# Flexible popup that 
def ErrorPopup():
    # Create new popup window with error notice
    newWindow = Toplevel(top)
    newWindow.title("Error")
    newWindow.geometry("100x55")

    Label(newWindow, text="Invalid Input").pack()

    # Button that closes popup window
    Button(newWindow, text="Got It", command=newWindow.destroy).pack()


# Tkninter main window
top = tkinter.Tk()

is_checked = tkinter.BooleanVar()

# This part looks bad because I followed a bad tutorial for my first tkinter project, better examples in ResultPopup func
L1 = Label(top, text="R6S Customs Manager",).grid(row=0,column=1)
L2 = Label(top, text="Operator Ban (Per Team)",).grid(row=1,column=0)
L3 = Label(top, text="Available Maps",).grid(row=2,column=0)
#L4 = Label(top, text="Symmetric Bans",).grid(row=3,column=0)
E1 = Entry(top, bd =1)
E1.grid(row=1,column=1)
E2 = Entry(top, bd =1)
E2.grid(row=2,column=1)
E3 = Entry(top, bd =1)
B1=Button(top, text ="Ready Up!", command=ResultPopup).grid(row=3,column=1,)
#C1 = tkinter.Checkbutton(top,variable=is_checked, onvalue=1, offvalue=0, command=Andor).grid(row=3,column=1) <- For asymmetric bans, ended up get scrapped

top.mainloop()

