#clear the screen
def cls() :
    print('\n' * 50)
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
#ask user if they wish to proceed
print ("Do you wish to continue with todays lesson ? ")
answer = input("Please input Y for yes, N for no : ")
# anything other than Y will quit program
if answer != "Y" :
    print ("OK "+ name +", Goodbye")
    quit
else :
    print ("OK "+ name +", lets continue :")
#to be continued
quit