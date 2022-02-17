import weaponClass as w
import csv

"""
- Craete a program that will read the contents of the file 'weapons.txt'. Each record in the file represents the specs to a weapon.
- Create an instance of the weapon object for each record. 
- Create a dictionary that will contain the name of the weapon as the key and the number of bullets as the value. 
- Print out details of each weapon using the object's methods only (as per comments below). 
- Fire all bullets of the weapon and print a countdown of bullets remaining (run exe file to visualize, HINT: use end='\r' in your print statement).
- Print out the name of the weapon and the number of bullets from the dictionary.

HINT: Follow the comments for each line to help with the logic of the problem.
"""


# create a file object to open the file in read mode
weapon_file = open("weapons.csv", "r")


# create a csv object from the file object
weapon_infile = csv.reader(weapon_file, delimiter=",")

# skip the header row

next(weapon_infile)


# create an empty dictionary named 'weapons_dict'
weapons_dict = {}


# use a for loop to iterate through every row of the csv file
for line in weapon_infile:
    # use variables for name,speed and range (optional)
    name = line[0]
    speed = line[1]
    Range = line[2]

    # create an instance of the weapon object using the
    # specs from the csv file (name,speed and range)
    user_weapon = w.Weapon(name, speed, Range)

    # append the name and bullet count to 'weapons_dict'
    user_weapon.set_bullets()
    weapons_dict["name"] = user_weapon.get_name()
    weapons_dict["count"] = user_weapon.get_bullets()
    print(weapons_dict)
    # print out the name of the weapon using the appropriate method of the object
    print(user_weapon.get_name())
    # print out the speed of the weapon using the appropriate method of the object
    print(user_weapon.get_speed())
    # print out the range of the weapon using the appropriate method of the object
    print(user_weapon.get_range())
    # print out the number of bullets of the weapon using the appropriate method of the object
    print(user_weapon.get_bullets())
    # use an input statement to halt the program and wait for the user -
    input("Press any key to fire the weapon")

    # use an appropriate loop to keep firing the weapon until all bullets run out
    bullets = user_weapon.get_bullets()
    while bullets > 0:
        # call the appropriate method to fire a bullet
        user_weapon.fire_bullet()
        bullets = user_weapon.get_bullets()
        # print out the bullet count every time the weapon is fired
        print(user_weapon.get_bullets(), end="\r")
    print(user_weapon.get_bullets())
    # using a loop print out the name and number of bullets from the dictionary
    # x = user_weapon.get_name
    for x in weapons_dict:
        print(x)
        print(weapons_dict[x])
