#Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

add_both = name1 + name2
lower_case = add_both.lower()

t = lower_case.count("t")
r = lower_case.count("r")
u = lower_case.count("u")
e = lower_case.count("e")

true = t + r + u + e

l = lower_case.count("l")
o = lower_case.count("o")
v = lower_case.count("v")
e = lower_case.count("e")

love = l + o + v + e

true_love = int(str(true + love))

if (true_love < 10) or (true_love > 90):
  print(f"Your  score is {true_love}, you go together like coke and mentos.")
elif (true_love >= 40) and (true_love <= 50):
  print(f"Your score is {true_love}, you are alright together.")
else:
  print(f"Your score is {true_love}")
