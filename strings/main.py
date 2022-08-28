# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
# Part 1 of assignment
# Variables for every player that scored
scorer_0 = 'Ruud Gullit'
scorer_1 = 'Marco van Basten'

# Variables for each minute of the match that a goal was scored
goal_0 = 32
goal_1 = 54

# Create a string that reports on who scored when and store it in a variable
scorers = scorer_0 + ' ' + str(goal_0) + ', ' + scorer_1 + ' ' + str(goal_1)

# Use f-string to create a string containing who scored when and store it in a variable
report = f'{scorer_0} scored in the {goal_0}nd minute\n{scorer_1} scored in the {goal_1}th minute'


# Part 2 of assignment
# Create a variable that contains the name a player that played in the soccer match
player = 'Frank Rijkaard'

# Use slicing and the find-method to isolate and store the player's first name
first_name = player[0:(player.find(' '))]

# Use the find-method, slicing and len to isolate and store the length of their last name
last_name = player[(player.find(' ') + 1):]
last_name_len = len(last_name)

# Isolate and store the player's name in this format: G. von Examplestein
name_short = f'{player[0:1]}. {last_name}'

# Chant the players firt name x-times, where x is the number of characters in the firt name and remove white space after last character
chant = ((first_name + '! ') * len(first_name)).rstrip()

# Check if last character of chant is not a white space
good_chant = chant[len(chant) - 1] != ' '