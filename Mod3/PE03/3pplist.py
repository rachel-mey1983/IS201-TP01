
# Make a list that includes at least three people you'd like to invite to dinner. Include the following in your code.
#	print the list with at least three people
#	Modify your list, replacing the name of one the guest who can't make it with the name of the new person you are inviting. Then print the new list.
#	Use insert() to add one new guest to the beginning of your list.
#	Use insert() to add one new guest to the middle of your list.
#	Use append() to add one new guest to the end of your list.
#	Print the new list
#	Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you're sorry you can't invite them to dinner. #####

def add_guest(guest_list, guest):
    guest_list.append(guest)  # Add the guest to the list
    print(f'Added guest:{guest}')  # Confirmation message

def remove_guest (guest_list, newguest):

    for guest in guest_list:  # Iterate through the list to find
        if guest[0] == newguest:
            guest_list.remove ( guest )  # Remove the guest from the list
            print ( f'Removed guest:{newguest}' )
            return
            #  Confirmation message
    print ( 'Unfortunately, I cannot extend an invitation to dinner.' )  # If the guest is not found in the list


def search_guest(guest_list, newguest):
    guest: object
    for guest in guest_list:  # Iterate through the list to find the guest
        if guest == newguest:
            print ( 'Found guest: {guest}' )
            return
    print ( 'guest Not Found.' )


def convert_to_tuples(guest_list):
    return [tuple ( guest ) for guest in guest_list]  #  Convert each dictionary to a tuple and return a list of tuples


def convert_to_lists(tuple_list):  # Convert each tuple to a list and return a list of lists
    return [list ( guest ) for guest in tuple_list]


guest_list = [['1984', 'George Orwell'], ['To Kill a Mockingbird', 'Harper Lee']]
guest_tuples = convert_to_tuples ( guest_list )  # Convert the list of guests to a list of tuples
guest_list_modifiable = convert_to_lists ( guest_tuples )  # Convert the list of tuples back to a list of lists


add_guest ( guest_list_modifiable,
           ['Lady Gaga, Josh Homme, Stevie Nicks'] )
remove_guest ( guest_list_modifiable,
              'Chris Cornell' )  # The erroneous call to undefined function 'add_guest'
# has been removed.remove_guest (guests_list_modifiable, '1984')
# Remove a guest from the list
search_guest ( guest_list_modifiable,
              'Chris Cornell' )

print ( 'Final guests list:' )
for guest in guest_list_modifiable:
    print ( guest )  # Print the final list of guests
