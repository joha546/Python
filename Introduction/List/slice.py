letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)

#replace with some values
letters[2:5]=['C','D','E']
print(letters)

#now remove them
letters[2:5]=[]
print(letters)

# clear the list by replacing all the elements with an empty list
letters[:] = []
print(letters)