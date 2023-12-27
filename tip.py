print("Welcome to Tip calculator you faggot")
bill = float(input("what was the total bill? "))
pertip=int(input("What percentage of total bill would you like to give 10, 12 or 15"))
people=int(input("How many people are splitting the bill"))
tip=(bill*(pertip/100))
newbill=(tip+bill/people)
print("Each person should pay "+str(round(tip,2)))


