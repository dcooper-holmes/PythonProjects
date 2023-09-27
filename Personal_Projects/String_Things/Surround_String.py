
string = "TEST"

print(f"{string}") #normal f string
print(f"{string:#<20}") #Adds 20 hashes to the right
print(f"{string:_>20}") #Adds 20 underscores to the left
print(f"{string:.^20}") #Surrounds string with 20 dots (10 either side)