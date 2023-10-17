# TODO: Write a prompt that asks users to "type something to win"
#       They will only win if they type "something" into the prompt
#
# Collect user input
# Compare to the string "something"
# Print a win or lose message

# Getting input
something = input ("type something to win: ")
# Setting the input to lower case
something = something.lower()

# Stating possibilities
if something == ("something"):
    print("congrats you won!")

else:
    print("try again!")