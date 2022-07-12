# 2 people paying 280 ROOM
# 8 people paying 260 BED
# total = 2640

# Rooms = 2
# Beds = 8

# HousePeopleTotal = 10
# HouseAmountTotal = (280*Rooms) + (260*Beds)
# print(f"House Amount Total = " + str(HouseAmountTotal))

# #Fern and Kuz paying 21% of the place
# #Everyone else paying 79%

# Total = 2640

# RoomsTotal = Total/Rooms
# BedsTotal = Total/Beds

# print("Room Total = " + str(RoomsTotal))
# print("Bed Total = " + str(BedsTotal))





# print("--------------------")


# totalCost = 1000
# Rooms = 2
# Beds = 8

# AdditinalPpl = 2

# PeopleTotal = Beds + Rooms

# RoomPplPercent = Rooms/PeopleTotal
# BedPplPercent = Beds/PeopleTotal

# print("Room People Percent = "+ str(RoomPplPercent))
# print("Bed People Percent = "+ str(BedPplPercent))

# BedPplTotalAmm = BedPplPercent * totalCost
# print("Bed People Total cost = " + str(BedPplTotalAmm))

# RoomPplTotalAmm = RoomPplPercent * totalCost
# print("Room People Total cost = " + str(RoomPplTotalAmm))

# print("Fern and Kuz each pay " + str(RoomPplTotalAmm/Rooms))
# print("Everyone else each pay str " + str(BedPplTotalAmm/Beds))

#testing






# print("-------------")

# FnK = .25
# EveryoneElse = .75

# FnkCost = FnK * totalCost
# print("Fern n Kuz total pay is " + str(FnkCost))
# EveryoneCost = EveryoneElse * totalCost
# print("Everyone else total pay is " + str(EveryoneCost))

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