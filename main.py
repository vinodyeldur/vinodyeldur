#LIFE IN WEEKS coding

age = input("What is your current age? ")

remaining = 90-int(age)
Days = int(remaining)*365 
months =int(remaining)*12
weeks = int(remaining)*52

message =  (f"You have {Days} days, {weeks} weeks, and {months} months left")
print(message)



