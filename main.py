# This is ment to be used by my friends to calculate the price of our AirBnb. I made this so we can easily make calculations.

# We have 2 bedrooms that people are paying a premium for. If every room was created equaly then we could easiy do some math to calculate the price. 

# But we need to take into account that certain people are paying different rates. This caculuator takes that into account


print("Hard Summer House Calculator by Anthony Omens")
print("This Calculator only works when we have More Than 10 people in the house")
print("----------------")

HouseCost = 2450

originalAmm = 10

FernAndKuzPay = 560
EveryElsePay = 1890


print("House total is " + str(HouseCost))
print("Fern n Kuzie pay " + str(FernAndKuzPay) + " total")
print("Everyone else pays " + str(EveryElsePay) + " total")

MorePeople = int(input("How many EXTRA people are coming?\nPlease input just the number\nMobile users press Return to enter number"))

NewTotal = originalAmm + MorePeople
print("With " + str(MorePeople) + " additional people we now have a total of " + str(NewTotal) + " people")

percentChange = originalAmm / NewTotal

percentChange = "{:.2f}".format(percentChange)

print("Percent change is now " + str(percentChange))

FernAndKuzPayWithNewPeople = (float(FernAndKuzPay) * float(percentChange)) + 1

print("Fern and Kuzie pay " + str(FernAndKuzPayWithNewPeople))
print("Fern and Kuzie each pay " +str(FernAndKuzPayWithNewPeople/2))

EveryElsePayNewPeople = HouseCost - FernAndKuzPayWithNewPeople

print("Remaing is now " + str(HouseCost - FernAndKuzPayWithNewPeople))

print("With everyone else adding up to a total of " + str(NewTotal - 2) + " everyone else must pay " + str((EveryElsePayNewPeople/NewTotal)))