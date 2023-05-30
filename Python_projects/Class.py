# Parent class
class Player:
    name = 'Erik' #Player atribute; the name of the player
    jersy_no = 10
    position = 'defender'
    team = ' '

# Child class. this will inhereit all of the behavior of the parent class
#with its own attributes 
class team_member(Player):
    email = ''
    phone_no = 123456

# Child class. this will inhereit all of the behavior of the parent class
# with its own attributes
class team_captain(Player):
    mailing_address = ' '
    responsibility_allowance = 16.00
