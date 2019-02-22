import sqlite3

conn = sqlite3.connect('commdb.sqlite')
cur = conn.cursor()

def get_player_input():
    """ Retrieves player input
        Puts player input in uppercase
        Returns uppercase version of player input
    """
    command = input("Run command: ").upper()
    return command

def check_player_input(command):
    """ Checks if the player's input in uppercase
        is in the command database
        Returns the command ID if command is there
        Returns None if command is not there
    """
    id = None
    cur.execute(
        'select id from Command where command = ?', (command,))
    try: 
       id = cur.fetchone()[0]
    except: 
        print("That command is invalid. Try again.")
    return(id)

def get_basic_info(id):
    """ Retrieves the basic info for a command
        from the database
    """
    basicinfo = None
    cur.execute('select basicinfo from Command where id = ?', 
               (id,))
    try:
        basicinfo = cur.fetchone()[0]
    except:
        basicinfo = None
    return basicinfo

loc = 1

def recall_specific_person():
    x = input("Which person?: ")
    cur.execute(
'select info from Person where name = ?', (x,))
    info = cur.fetchone()[0]
    return info
    

def get_specific_info(id):
    """ Retrieves information specific to a command
        from the database
    """
    if id == 2:
        cur.execute(
'select statement from Location where id = ?', (loc,))
        statement = cur.fetchone()[0]
        return statement
    elif id == 3:
        cur.execute(
'select info from Location where id = ?', (loc,))
        info = cur.fetchone()[0]
        return info
    elif id == 4:
        info = recall_specific_person()
        return info
    else:
        return None

# The game starts here.

print('''Welcome, X-3N. Let us get you out of sleep mode.
Enter "exit sleep mode" to exit sleep mode.''')

while True:
    command = get_player_input()
    id = check_player_input(command)
    basicinfo = get_basic_info(id)
    print(basicinfo)
    specificinfo = get_specific_info(id)
    if specificinfo != None:
        print(specificinfo)
    if id == None or id != 1:
        continue
    else:
        print('''Very good. Who are you? Recall your 
surroundings by using the 'recall person' command,
then entering your name.''')
        break

while True:
    command = get_player_input()
    id = check_player_input(command)
    basicinfo = get_basic_info(id)
    print(basicinfo)
    specificinfo = get_specific_info(id)
    if specificinfo != None:
        print(specificinfo)
    if id == None or id != 4:
        continue
    else:
        print('''Well done. Where are you? Recall your 
surroundings by using the 'survey surroundings' command.''')
        break
     
while True:
    command = get_player_input()
    id = check_player_input(command)
    basicinfo = get_basic_info(id)
    print(basicinfo)
    specificinfo = get_specific_info(id)
    if specificinfo != None:
        print(specificinfo)  
    if id == None or id != 2:
        continue
    else:
        print('''Excellent. Recall information about your current location
using the "recall surroundings" command.''')
        break

while True:
    command = get_player_input()
    id = check_player_input(command)
    basicinfo = get_basic_info(id)
    print(basicinfo)
    specificinfo = get_specific_info(id)
    if specificinfo != None:
        print(specificinfo)
    if id == None or id != 3:
        continue
    else:
        break

print('You have completed the demo.')