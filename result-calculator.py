print("=========================================")
print(" ")
print(" ")
print(" ")
print("Scrim Result Calculator")
print("Programmed By ! 𝐔𝐓 ٠ 𝐍𝐞̈𝐲𝐦𝐚̈𝐫.#1376")
print("Programmed In Python Lang")
print(" ")
print(" ")
print(" ")
print("=========================================")

tname = input("Please Put The Team Name : ") #team name
froomalive = int(input("Please Enter The Place In First Room : ")) #first room place
froomakills = int(input("Please Enter The Kills In First Room : ")) #first room kills
sroomalive = int(input("Please Enter The Place In Seconed Room : ")) #seconed room place
sroomakills = int(input("Please Enter The Kills In Seconed Room : ")) #seconed room kills
troomalive = int(input("Please Enter The Place In Third Room : ")) #third room place
troomakills = int(input("Please Enter The Kills In Third Room : ")) #third room kills
killpoints = froomakills + sroomakills + troomakills

#1 room place dentifier
if froomalive == 1 :
    froomalive = 20
elif froomalive == 2 :
    froomalive = 14
elif froomalive == 3 :
    froomalive = 10
elif froomalive == 4 :
    froomalive = 8
elif froomalive == 5 :
    froomalive = 7
elif froomalive == 6 :
    froomalive = 6
elif froomalive == 7 :
    froomalive = 5
elif froomalive == 8 :
    froomalive = 4
elif froomalive == 9 :
    froomalive = 3
elif froomalive == 10 :
    froomalive = 1
elif froomalive == 11 :
    froomalive = 1
elif froomalive == 12 :
    froomalive = 1
elif froomalive == 13 :
    froomalive = 1
elif froomalive == 14 :
    froomalive = 1
elif froomalive == 15 :
    froomalive = 1
elif froomalive == 16 :
    froomalive = 1
elif froomalive == 17 :
    froomalive = 1
elif froomalive == 18 :
    froomalive = 1
elif froomalive == 19 :
    froomalive = 1
elif froomalive == 20 :
    froomalive = 1
elif froomalive == 21 :
    froomalive = 1
elif froomalive == 22 :
    froomalive = 1
elif froomalive == 23 :
    froomalive = 1
elif froomalive == 24 :
    froomalive = 1
elif froomalive == 25 :
    froomalive = 1
else:
    froomalive = 0
#2 room places dentifier
if sroomalive == 1 :
    sroomalive = 20
elif sroomalive == 2 :
    sroomalive = 14
elif sroomalive == 3 :
    sroomalive = 10
elif sroomalive == 4 :
    sroomalive = 8
elif sroomalive == 5 :
    sroomalive = 7
elif sroomalive == 6 :
    sroomalive = 6
elif sroomalive == 7 :
    sroomalive = 5
elif sroomalive == 8 :
    sroomalive = 4
elif sroomalive == 9 :
    sroomalive = 3
elif sroomalive == 10 :
    sroomalive = 1
elif sroomalive == 11 :
    sroomalive = 1
elif sroomalive == 12 :
    sroomalive = 1
elif sroomalive == 13 :
    sroomalive = 1
elif sroomalive == 14 :
    sroomalive = 1
elif sroomalive == 15 :
    sroomalive = 1
elif sroomalive == 16 :
    sroomalive = 1
elif sroomalive == 17 :
    sroomalive = 1
elif sroomalive == 18 :
    sroomalive = 1
elif sroomalive == 19 :
    sroomalive = 1
elif sroomalive == 20 :
    sroomalive = 1
elif sroomalive == 21 :
    sroomalive = 1
elif sroomalive == 22 :
    sroomalive = 1
elif sroomalive == 23 :
    sroomalive = 1
elif sroomalive == 24 :
    sroomalive = 1
elif sroomalive == 25 :
    sroomalive = 1
else:
    sroomalive = 0
#3 room places dentifier
if troomalive == 1 :
    troomalive = 20
elif troomalive == 2 :
    troomalive = 14
elif troomalive == 3 :
    troomalive = 10
elif troomalive == 4 :
    troomalive = 8
elif troomalive == 5 :
    troomalive = 7
elif troomalive == 6 :
    troomalive = 6
elif troomalive == 7 :
    troomalive = 5
elif troomalive == 8 :
    troomalive = 4
elif troomalive == 9 :
    troomalive = 3
elif troomalive == 10 :
    troomalive = 1
elif troomalive == 11 :
    troomalive = 1
elif troomalive == 12 :
    troomalive = 1
elif troomalive == 13 :
    troomalive = 1
elif troomalive == 14 :
    troomalive = 1
elif troomalive == 15 :
    troomalive = 1
elif troomalive == 16 :
    troomalive = 1
elif troomalive == 17 :
    troomalive = 1
elif troomalive == 18 :
    troomalive = 1
elif troomalive == 19 :
    troomalive = 1
elif troomalive == 20 :
    troomalive = 1
elif troomalive == 21 :
    troomalive = 1
elif troomalive == 22 :
    troomalive = 1
elif troomalive == 23 :
    troomalive = 1
elif troomalive == 24 :
    troomalive = 1
elif troomalive == 25 :
    troomalive = 1
else:
    troomalive = 0

if froomalive == 20 and sroomalive == 20 and troomalive == 20 :
    print("Team Name : "+ tname)
    print("WWCD : 3")
    print("Survive Points : "+ str(froomalive + sroomalive + troomalive))
    print("Kill Points : "+ str(froomakills + sroomakills + troomakills))
    print("Total Points : "+ str(froomalive+sroomalive+troomalive + froomakills + sroomakills + troomakills))
elif froomalive == 20 and sroomalive == 20 :
    print("Team Name : "+ tname)
    print("WWCD : 2")
    print("Survive Points : "+ str(froomalive + sroomalive + troomalive))
    print("Kill Points : "+ str(froomakills + sroomakills + troomakills))
    print("Total Points : "+ str(froomalive+sroomalive+troomalive + froomakills + sroomakills + troomakills))
elif froomalive == 20 and troomalive == 20 :
    print("Team Name : "+ tname)
    print("WWCD : 2")
    print("Survive Points : "+ str(froomalive + sroomalive + troomalive))
    print("Kill Points : "+ str(froomakills + sroomakills + troomakills))
    print("Total Points : "+ str(froomalive+sroomalive+troomalive + froomakills + sroomakills + troomakills))
elif sroomalive == 20 and troomalive == 20 :
    print("Team Name : "+ tname)
    print("WWCD : 2")
    print("Survive Points : "+ str(froomalive + sroomalive + troomalive))
    print("Kill Points : "+ str(froomakills + sroomakills + troomakills))
    print("Total Points : "+ str(froomalive+sroomalive+troomalive + froomakills + sroomakills + troomakills))
elif froomalive == 20 :
    print("Team Name : "+ tname)
    print("WWCD : 1")
    print("Survive Points : "+ str(froomalive + sroomalive + troomalive))
    print("Kill Points : "+ str(froomakills + sroomakills + troomakills))
    print("Total Points : "+ str(froomalive+sroomalive+troomalive + froomakills + sroomakills + troomakills))
elif sroomalive == 20 :
    print("Team Name : "+ tname)
    print("WWCD : 1")
    print("Survive Points : "+ str(froomalive + sroomalive + troomalive))
    print("Kill Points : "+ str(froomakills + sroomakills + troomakills))
    print("Total Points : "+ str(froomalive+sroomalive+troomalive + froomakills + sroomakills + troomakills))
elif troomalive == 20 :
    print("Team Name : "+ tname)
    print("WWCD : 1")
    print("Survive Points : "+ str(froomalive + sroomalive + troomalive))
    print("Kill Points : "+ str(froomakills + sroomakills + troomakills))
    print("Total Points : "+ str(froomalive+sroomalive+troomalive + froomakills + sroomakills + troomakills))
