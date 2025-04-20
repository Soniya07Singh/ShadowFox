# LIST MANIPULATION
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
num_members = len(justice_league)    #len is used to find the length of the list.
print("1. Number of members:", num_members)

justice_league.append("Batgirl")      #append is used to add an element to the end of list. one at a time.
justice_league.append("Nightwing")
print("2. List after adding Batgirl and Nightwing:", justice_league)

justice_league.remove("Wonder Woman")    #remove is used to remove an element from the list. from anywhere.
print(" list after removing Wonder Women:", justice_league)

justice_league.insert(0, "Wonder Woman")   # insert is used to add an element at a specific index.
print("3. Wonder Woman is now the leader:", justice_league)

justice_league.remove("Superman")    #remove is to remove an element from the list.
flash_index = justice_league.index("Flash")  #index is used to find the index of an element from the list.
aquaman_index = justice_league.index("Aquaman")
insert_index = max(flash_index, aquaman_index)      #max is used to find the maximum of two numbers.
#here it is used to find the maximum in the index of flash and aquaman.
justice_league.insert(insert_index, "Superman")   # we are inserting superman at the index of maximum of flash and aqauman.
print("4. After separating Aquaman and Flash:", justice_league)

justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("5. New team assembled:", justice_league)

justice_league.sort()
print("6. Justice League sorted alphabetically:", justice_league)
print("   New leader is:", justice_league[0])


#------------------------output-----------------------
#1. Number of members: 6
#2. List after adding Batgirl and Nightwing: ['Superman', 'Batman', 'Wonder Woman', 'Flash', 'Aquaman', 'Green Lantern', 'Batgirl', 'Nightwing']
 #list after removing Wonder Women: ['Superman', 'Batman', 'Flash', 'Aquaman', 'Green Lantern', 'Batgirl', 'Nightwing']
#3. Wonder Woman is now the leader: ['Wonder Woman', 'Superman', 'Batman', 'Flash', 'Aquaman', 'Green Lantern', 'Batgirl', 'Nightwing']
#4. After separating Aquaman and Flash: ['Wonder Woman', 'Batman', 'Flash', 'Superman', 'Aquaman', 'Green Lantern', 'Batgirl', 'Nightwing']
#5. New team assembled: ['Cyborg', 'Shazam', 'Hawkgirl', 'Martian Manhunter', 'Green Arrow']
#6. Justice League sorted alphabetically: ['Cyborg', 'Green Arrow', 'Hawkgirl', 'Martian Manhunter', 'Shazam']
 #  New leader is: Cyborg