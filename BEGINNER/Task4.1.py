# FINDING LENGTH OF EACH NAME IN A LIST 
friends = ["Aditya", "Riya", "Siddharth", "Neha", "Kabir"]    #list of friends.

name_lengths = [(name, len(name)) for name in friends] #len is used to get the length of the string.
#here we r using list comprehension to create a list of tuples.
print(name_lengths)

#-----------------------OUTPUT-----------------------
#[('Aditya', 6), ('Riya', 4), ('Siddharth', 9), ('Neha', 4), ('Kabir', 5)]