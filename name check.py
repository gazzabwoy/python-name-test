#ask user to input forename and surname
name = input ("What is your Forename: ")
surname = input ("What is your Surname : ")
#unless your me your paying £10
if name == "Gary" and surname == "Duffner" :
    status = "the owner"
    price = "free"
else : 
    status = "a user"
    price = "ten pounds"
#printing out price
print ("Welcome "+ name +" "+ surname )
print ("As "+ status +", todays lessons will be " +price)
print ("Do you wish to continue with todays lesson ? ")
answer = input("Please input Y for yes, N for no : ")
if answer != "Y" :
    quit
else :
    print ("OK lets continue")
